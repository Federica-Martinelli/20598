# NGOs Smart Contract - 20598

## Getting Started
For this project we implemented a __smart contract__ with the aim of applying __blockchain technology__ to the __NGO world__ as a group assignment for the Bocconi University course _Fintech and Blockchains - 20598_.

The main purpose is to __combat fraud and increase people's trust in NGOs__.

The key aspect of the contract is that it allows NGOs to create __projects__ characterized by an __immutable mission, location, goal and deadline__. Moreover, __donors can send__ their __preferred amount__ to a particular project until the its goal is reached or until the deadline is passed. Finally, the contract includes a __consensus-based payment function__ as a __safety feature__ to combat embezzlement. This means that, once the whole amount needed for a project has been collected, the __NGO__ that posted the project can only __ask to withdraw a certain amount__ if a pool of __"information miners"__ (other NGOs or banks) approves this transaction.

The __Solidity contract compiled in Remix__ is contained in a __.txt file__ (`contract.txt`) while a __Python implementation__ of the contract is contained in a __Jupyter Notebook__(`using_contract.ipynb`).

## Prerequisites
To run the notebook a __Ganache application__ needs to be opened to simulate different ether wallets. 
__Keys and server urls__ also need to be adjusted.

Additionally, the __coinapi key__ is the free version and only allows for 100 requests per day. If passed, it is possible to retrieve a free key on the website: https://www.coinapi.io/

## Project Organization
The __files__ for this project are organized in the following way:

1.  Folder __documentation__:
    *  __contrib.md__: Daily tasks carried out by the team to complete the project
    *  __project_evolution.md__: More complete documentation regarding the logic that was used to develop the project    
    
2.  Folder __summary__:
    *  __NGOs_fintech.pdf__: Presentation which explains our project in a more complete way
    
3.  Folder __scr__:
    *  __final_version__:
        *  __contract.txt__: Solidity contract coded and compiled in Remix official Ethereum compiler
        *  __using_contract.ipynb__: Example showcasing the various steps to use the contract
        *  __json_files__: Folder containing json files of the compiled contract
        *  __INSTALL.md__: Explains how to run the code 
    *  __past_versions__:
        *  __ngo_blockchain__: Folder containing code to create our own blockchain (this project was abandoned)
        *  __smart_contract__: Folder containing a previous version of the smart contract and of the notebook to try its features
