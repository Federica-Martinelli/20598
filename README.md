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
