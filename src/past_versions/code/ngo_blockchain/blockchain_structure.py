# -----------------------------------------------------------------
#  Toy Blockchain for DSBA 20598 FinTech and Blockchain course
#  (c) 2019 Silvio Petriconi <myfirstname.mylastname@unibocconi.it>
#  License: GNU General Public License 3.0
# -----------------------------------------------------------------

import hashlib
import datetime
from collections import namedtuple
import binascii
from PyScripts.utils import merkle
import struct
import pandas as pd
import json
from time import time
from urllib.parse import urlparse
from uuid import uuid4
import random
import string
import os

import requests
from flask import Flask, jsonify, request

GENESIS_ROOT_DATA = [binascii.unhexlify('0000DEADBEEFBADCAFFEBAADF00D')]  # TODO: is this random
GENESIS_ROOT_NONCE = 0
GENESIS_NONCE = 101  # FIXME --> is this random
GENESIS_DIFFICULTY = 1

# Every block header is a namedtuple, immutability is automatically enforced.
Blockheader = namedtuple('Blockheader', \
                         'height prev timestamp difficulty merkleroot nonce')

# Data for the genesis block. It has no previous, so the prev hash is zero.
_genesisblock = Blockheader(
    height=0,
    prev=binascii.unhexlify('0000000000000000000000000000000000000000000000000000000000000000'),
    timestamp=1572328964,
    difficulty=GENESIS_DIFFICULTY,
    merkleroot=merkle.MerkleTree(GENESIS_ROOT_DATA).digest(),
    nonce=GENESIS_NONCE
)


class Blockchain:
    def __init__(self, genesis=_genesisblock, hashfunc=None):
        self._blockhdrs = []  # list of block headers
        self._blockindex = {}  # dict that maps blockheader hash to index
        self._hashfunc = hashfunc if hashfunc else lambda x: hashlib.sha256(x).digest()
        self._difficulty = GENESIS_DIFFICULTY
        self._append_block(genesis)  # append genesis block

        self.current_transactions = []
        self.fund_df = pd.DataFrame(index='trans_id',
                                    columns=['sender', 'receiver', 'amount', 'project', 'country', 'continent',
                                             'max_time'])
        self.ngo_company = 'random_company_name'  # would be the NGO using the chain
        self.project_info = {}  # TODO: dict with approved name of companies working on project
        self.error_message = ''
        self.nodes = set()
        self.hashes = []  # list of current block transaction hashes

    def register_node(self, address):
        """
        Add a new node to the list of nodes

        :param address: <str> Address of node. Eg. 'http://192.168.0.5:5000'
        :return: None
        """

        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def create_blockheader(self, merkleroot, nonce):
        '''
        Creates a block candidate for the blockchain.
        :merkleroot: the merkle root of the block's data
        :param nonce: the nonce that generates a valid block hash
        :returns: the new block (without appending it to the chain)
        '''
        # compute hash of previous block
        if len(self._blockhdrs) > 0:
            prevhash = self._hashfunc(self._serialize_hdr(self._blockhdrs[-1]))
        else:
            # Genesis block has hash over empty set as previous field.
            prevhash = self._hashfunc(b'')

        thisBlock = Blockheader(
            height=len(self._blockhdrs),
            prev=prevhash,
            timestamp=int(datetime.datetime.now().timestamp()),
            difficulty=self._difficulty,
            merkleroot=binascii.hexlify(merkleroot),
            nonce=nonce)
        return thisBlock

    def create_new_transaction(self, fund_data, trans_id, sender, recipient, amount, type, distribution=None,
                               project=None,
                               country=None, continent=None, genre=None):

        self.current_transactions.append({
            'fund_data': fund_data,
            'ID': trans_id,
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            'distribution': distribution,
            'project': project,
            'country': country,
            'continent': continent,
            'type': type,
            'genre': genre,
        })

        return self.last_block['index'] + 1

    def _serialize_hdr(self, blockhdr):
        # serializes a block header to binary format (big endian):
        # struct Blockheader {
        #     uint64             height;
        #     char[32]           prev;
        #     uint64             timestamp;
        #     uint64             difficulty;
        #     char[32]           merkleroot;
        #     uint64             nonce;
        # }
        return struct.pack(">I32sII32sI", *blockhdr)

    def _deserialise_hdr(self, bindata):
        # returns a block header from serialized binary data, without
        # checking its validity in any way
        return Blockheader._make(struct.unpack(">I32sII32sI", bindata))

    def _append_block(self, blockheader):
        # actually appends block header without checking it
        blockhash = self._hashfunc(self._serialize_hdr(blockheader))
        if blockhash in self._blockindex:
            raise RuntimeError(f"Block {blockhash} already inserted.")
        print("Block hash: ", blockhash)

        # if all checkes go through, save block hash in a dict
        blockheight = len(self._blockhdrs)
        self._blockindex[blockhash] = blockheight
        self._blockhdrs.append(blockheader)
        return blockheight

    def can_append(self, block, diagnostics=False):
        '''
        Checks whether a candidate block is valid and can be
        appended to the chain.
        :param block: candidate block to be verified
        :param diagnostics: if set True, returns diagnostics
        :returns: True if block is valid, False otherwise. If
        diagnostics is True, returns a tuple (valid, errorstring).
        '''
        if block.height != len(self._blockhdrs) or \
                block.prev != self._hashfunc(self._serialize_hdr(self._blockhdrs[-1])):
            return (False, "Bad block: block height or prev block invalid.") \
                if diagnostics else False

        if block.prev not in self._blockindex:
            return (False, "Bad prev hash pointer: prev block not in chain.") \
                if diagnostics else False

        if self._blockindex[block.prev] != len(self._blockhdrs) - 1:
            return (False, "Can't append block: prev isn't at end of chain.") \
                if diagnostics else False

        # then, check that difficulty is set appropriately
        if self._difficulty != block.difficulty:
            return (False, "Block difficulty is not at current level.") \
                if diagnostics else False

        if not self._blockhash_matches_difficulty(block):
            raise ValueError(
                "Block hash POW not commensurate to difficulty.")  # TODO: no need for POW as we wont combat
            # cyberattacks but we could set to a low difficulty to avoid spam or something
        #
        # if not self._blocktransaction_is_complete(block):
        #     raise ValueError(self.error_message)
        #
        # if not self._blocktransaction_matches_contracts(block):
        #     raise ValueError(self.error_message)

        # TODO: check nodes

        return (True, '') if diagnostics else True

    def append_block(self, block):
        '''
        :param block: block to be appended
        :returns: the height of the new blockchain. Raises RuntimeError
        if the block was already inserted or ValueError if the block
        is not a valid continuation of the chain.
        '''

        # first, validate that the block height is n+1 and
        # that prev hash points to the last block on chain
        append_ok, errormsg = self.can_append(block, diagnostics=True)

        if not append_ok:
            raise ValueError(errormsg)

        return self._append_block(block)

    def _blockhash_matches_difficulty(self, blockhdr):
        hexHashstring = str(binascii.hexlify(self._hashfunc(self._serialize_hdr(blockhdr))))
        return hexHashstring.startswith('0' * self._difficulty)

    def _blocktransaction_matches_contracts(self):
        # check if this is money given to NGO or NGO giving to project
        for transaction in self.current_transactions:
            # if so than accept block into chain since its a donation
            if transaction['receiver'] == self.ngo_company:
                return True

            # if  not run tests
            else:
                # check if receiver is part of project
                if transaction['receiver'] not in self.project_info[transaction['project']]['companies']:
                    self.error_message = 'Receiving party not approve.'
                    return False

                # check if continent, country and type match project
                if transaction['genre'] != self.project_info[transaction['project']]['genre']:
                    self.error_message = 'Project or Type of transaction not correct.'
                    return False

                if transaction['continent'] != self.project_info[transaction['project']]['continent']:
                    self.error_message = 'Project or Continent of transaction not correct.'
                    return False

                if transaction['country'] != self.project_info[transaction['project']]['country']:
                    self.error_message = 'Project or Country of transaction not correct.'
                    return False

                # check if the money is in accordance with customer digital contract
                else:
                    for key in transaction['distribution'].keys():
                        # get client data
                        temp = transaction['fund_data'].loc[key]

                        # check if client wanted to donate for this project
                        if transaction['project'] in temp.project:
                            temp = temp[temp.project == transaction['project']]
                            # if so check if amount and due date are correct
                            if temp.amount.sum() < transaction['distribution'][key]:
                                self.error_message = 'A donor does not have the funds to allocate to this project.'
                                return False

                            elif temp.amount.sum() >= transaction['distribution'][
                                key] and (
                                    temp.max_time.any() < int(
                                datetime.datetime.now().timestamp()) or temp.max_time.any() is not None):  # TODO: check if works its for when they dont have a time restriction
                                self.error_message = 'A donor has past his maximum time limit on the donation.'
                                return False

                            else:
                                return True
                        # if client has not specified the project, is he willing to give to this sort of project
                        else:
                            # TODO: find better filter mechanism
                            # filter preferences and allow for none preference
                            temp = temp[temp.country.isin([transaction['country'], None])]
                            temp = temp[temp.continent.isin([transaction['continent'], None])]
                            temp = temp[temp.genre.isin([transaction['genre'], None])]

                            # check if amount and due date are correct
                            if temp.amount.sum() < transaction['distribution'][key]:
                                self.error_message = 'A donor does not have the funds to allocate to this project.'
                                return False

                            elif temp.amount.sum() >= transaction['distribution'][
                                key] and (
                                    temp.max_time.any() < int(
                                datetime.datetime.now().timestamp()) or temp.max_time.any() is not None):  # TODO: check if works its for when they dont have a time restriction
                                self.error_message = 'A donor has past his maximum time limit on the donation.'
                                return False

                            else:
                                return True

    def _blocktransaction_is_complete(self):
        # check if block has at least one giving and one receiving and that they match
        if (self.current_transactions[0].type == 1 and self.current_transactions[1] == 1) or (
                self.current_transactions[0] == 0 and self.current_transactions[1] == 0):
            self.error_message = 'Transaction pair is not receiving and giving.'
            return False

        # check if all the info matches
        for i in range(len(self.current_transactions[0])):
            if self.current_transactions[0][i] != self.current_transactions[1][i]:
                self.error_message = 'Transaction pair does not have matching data.'
                return False

    def _blocktransaction_matches_fund_data(self, blockhdr, blockhdr_past):
        # filter new transactions
        last_test = blockhdr.transactions['fund_data'].drop(lambda x: x['trans_id'] in blockhdr.transactions,
                                                            inplace=True)

        if blockhdr_past.transactions['fund_data'] != last_test:
            return False

    def hash_transactions(self):
        for trans in self.current_transactions:
            # create a hash of all the info in a transaction
            self.hashes.append(self._hashfunc(self._serialize_hdr(trans)))

    def get_merkleroot(self):
        return self._hashfunc(self._serialize_hdr(self.hashes))



    def get_block_by_hash(self, its_hash):
        '''
        Finds a block by its hash value.
        :param its_hash:  (binary) hash value of the block
        :returns: the block if it exists in the chain, otherwise None.
        '''
        if its_hash in self._blockindex:
            return self._blockhdrs[self._blockindex[its_hash]]
        else:
            return None

    def is_valid(self, chain):
        """
        Determine if a given blockchain is valid

        :param chain: <list> A blockchain
        :return: <bool> True if valid, False if not
        """

        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            print("\n-----------\n")
            # Check that the hash of the block is correct
            if block['prev'] != self._hashfunc(last_block):
                return False

            # check nonce is correct
            if not self._blockhash_matches_difficulty(block, last_block):
                return False

            last_block = block
            current_index += 1

        return True

    def get_block(self, n):
        '''
        Obtains a block.
        :param n: the index of the block to be obtained
        :returns: the n-th block in the chain (0=genesis), None if not existent
        '''
        return self._blockhdrs[n] if n < len(self._blockhdrs) else None

    def update_fund_data(self, block):
        # online update on transaction that is a money flow, the other being more of a receipt
        for trans in block.transations:
            if trans['type'] == 0:
                donation = trans

        # change to negative amount for outgoing transaction
        if donation['recipient'] == self.ngo_company:
            donation['amount'] = - donation['amount']

        # update
        temp_df = pd.DataFrame(
            [donation['sender'], donation['receiver'], donation['amount'], donation['project'], donation['country'],
             donation['continent'], donation['max_time']], index=donation['trans_id'],
            columns=['sender', 'receiver', 'amount', 'project', 'country', 'continent', 'max_time'])

        self.fund_df.append(temp_df)

    @property
    def last_block(self):
        return self._blockhdrs[-1]

    def resolve_conflicts(self):
        """
        This is our consensus algorithm, it resolves conflicts
        by replacing our chain with the longest one in the network.

        :return: <bool> True if our chain was replaced, False if not
        """

        neighbours = self.nodes
        new_chain = None

        # We're only looking for chains longer than ours
        max_length = len(self._blockhdrs)

        # Grab and verify the chains from all the nodes in our network
        for node in neighbours:
            response = requests.get(f'http://{node}/chain')

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                # Check if the length is longer and the chain is valid
                if length > max_length and self.is_valid(chain):
                    max_length = length
                    new_chain = chain

        # Replace our chain if we discovered a new, valid chain longer than ours
        if new_chain:
            self._blockhdrs = new_chain
            return True

        return False

    def proof_of_work(self, last_block):
        nonce = 0
        while True:
            if self._blockhash_matches_difficulty(last_block):
                return nonce
            nonce += 1


if __name__ == '__main__':
    B = Blockchain()
    nonce = 0
    while True:
        g = Blockheader(height=_genesisblock.height,
                        prev=_genesisblock.prev,
                        timestamp=_genesisblock.timestamp,
                        difficulty=_genesisblock.difficulty,
                        transactions=_genesisblock.transactions,
                        merkleroot=_genesisblock.merkleroot,
                        nonce=nonce)
        print(f"Nonce: {nonce} Hash: ", binascii.hexlify(B._hashfunc(B._serialize_hdr(g))))
        if B._blockhash_matches_difficulty(g):
            print("======= FOUND GENESIS NONCE: =========", nonce)
            break
        nonce += 1


def create_blockchain_process(in_port):
    # Generate a globally unique address for this node
    node_identifier = '%s%04d' % (str(uuid4()).replace('-', ''), in_port)
    # Instantiate the Node
    app = Flask(node_identifier)
    # Instantiate the Blockchain
    blockchain = Blockchain()

    @app.route('/mine', methods=['GET'])
    def mine():
        # We run the proof of work algorithm to get the next proof...
        last_block = blockchain.last_block
        last_nonce= last_block['nonce']
        nonce = blockchain.proof_of_work(last_proof)

        # We must receive a reward for finding the proof.
        # The sender is "0" to signify that this node has mined a new coin.
        blockchain.new_transaction(
            sender="0",
            recipient=node_identifier,
            amount=1,
        )

        # Forge the new Block by adding it to the chain
        block = blockchain.new_block(proof)

        response = {
            'message': "New Block Forged",
            'index': block['index'],
            'transactions': block['transactions'],
            'proof': block['proof'],
            'previous_hash': block['previous_hash'],
        }
        return jsonify(response), 200

    @app.route('/transactions/new', methods=['POST'])
    def new_transaction():
        values = request.get_json()

        # Check that the required fields are in the POST'ed data
        required = ['fund_data', 'sender', 'recipient', 'amount', 'type']
        if not all(k in values for k in required):
            return 'Missing values', 400

        # assign random id to transation
        values['trans_id'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

        # Create a new Transaction
        index = blockchain.create_new_transaction(values['fund_data'], values['trans_id'], values['sender'],
                                                  values['recipient'], values['amount'], values['type'])

        response = {'message': f'Transaction will be added to Block {index}'}
        return jsonify(response), 201

    @app.route('/chain', methods=['GET'])
    def full_chain():
        response = {
            'chain': blockchain._blockhdrs,
            'length': len(blockchain._blockhdrs),
        }
        return jsonify(response), 200

    @app.route('/nodes/register', methods=['POST'])
    def register_nodes():
        values = request.get_json()

        nodes = values.get('nodes')
        if nodes is None:
            return "Error: Please supply a valid list of nodes", 400

        for node in nodes:
            blockchain.register_node(node)

        response = {
            'message': 'New nodes have been added',
            'total_nodes': list(blockchain.nodes),
        }
        return jsonify(response), 201

    @app.route('/nodes/resolve', methods=['GET'])
    def consensus():
        replaced = blockchain.resolve_conflicts()

        if replaced:
            response = {
                'message': 'Our chain was replaced',
                'new_chain': blockchain._blockhdrs
            }
        else:
            response = {
                'message': 'Our chain is authoritative',
                'chain': blockchain._blockhdrs
            }

        return jsonify(response), 200

    app.run(host='0.0.0.0', port=in_port)
    os._exit(0)
