# 20598 - FinTech for NGOs

## Getting Started
For this university project we implemented a smart contract with the aim of applying blockchain technology to the NGO world.
The main purpose is to combat fraud and increase people's trust in NGOs.

The key aspect of the contract is its immutable mission, location, goal and deadline once deployed as well as the presence of a consensus-based payment function as a safety feature to combat embezzlement.

The code is contained in a Jupyter Notebook.

## Prerequisites
If you desire to run the notebook you will need to open a Ganache application to simulate different ether wallets. 
You will also need to adjust keys and server urls.
Additionally, the coinapi key is the free version and only allows for 100 requests per day, if passed, please retrieve your own free key on the website: https://www.coinapi.io/

## Project Organization
The files for this project are organized in the following way:
1.  Folder __notebooks__: Contains 2 files:
    *  __Contract__: Contains the Solidity contract coded and compiled in Remix official Ethereum compiler. The contract is in .txt format 
    *  __Using_Contract__: Contains an example showcasing the various steps to use the contract. The file is in .ipynb format. 
2.  Folder __json_files__: Contains 2 files storing the metadata of the contract :
    *  __abi_v2.json__
    *  __bytecode_v2.json__
3.  Folder __past_versions__: Contains the past versions of the presentation and of the code. For the most part, the code was updated in place   
4.  File __Contributors_Information.txt__: Contains the daily tasks carried out by the team to complete the project 
5.  File __NGOs_Fintech.pdf__: Contains the presentation/report which explains our project in a more complete way

