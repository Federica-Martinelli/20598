# PROJECT EVOLUTION

The main steps that were taken to create the final smart contract are the following:

1.  __Creation of the virtual environment and installation of all necessary packages and software__:

*  This step consisted mainly in finding the best way to deploy a contract on a local chain so as to be able to test it on the language the project team was most used to: Python. 
*  Initial tests were made on the `infura.io` server host with `MetaMask chrome extension` for ease of multiple computer contributions.
*  The project contract deployment was then transferred for final tests and sample run notebook to `Ganache` to profit from multiple testing wallets. 
*  The main package used to interact with the contract was the `Web3 package` available on multiple programming languages (here python).

2.  __The starting point was a premade fundraising contract found on Github__:
 *  The link to this contract is: https://github.com/ankitbrahmbhatt1997/Ethereum_real_life_examples
 *  The author of this Github provided 3 samples of main uses for smart contracts being __Auction__, __Lottery__ and __Fundraising__. Considering our project focus is the implementation of Blockchain technology for NGOs, we used the latter contract as our __building block__.
 
3. __Creation of the main functions --> payable and PoW social consensus__:
*  Most of the initial work for this step was going through different forums (stackoverflow, Kaggle, etc.) to understand how `require() callbacks` are implemented in solidity smart contracts.
*  After that, the task for the __payable function__ was fairly straight-forward, as most of the simple smart contracts have similar payable functions with differing requirements.
*  An __only admin modifier__ was also implemented as found in most smart contracts.
*  The __Proof-of-Work social consensus__ based on information miners voting to allow expenses using the funds gathered was a trickier endeavour. As solidity is not meant for calculations but mostly storing data and filtering/requiring inputs, the use of __structures__, __mappings__ and __arrays__ seemed like the best option to keep track of all inputs made by various addresses. 
*  To understand the different aspects of these types in solidity, several well-made websites and forums, such as the following, were used:
  *  https://coursetro.com/posts/code/102/Solidity-Mappings-&-Structs-Tutorial
  *  https://medium.com/upstate-interactive/mappings-arrays-87afc697e64f
*  For information on how each of this were used in the code please refer to the report and corresponding comments in the solidity contract and/or testing notebook

4. __SCRAPTED – Transferring unused funds__:
*  To avoid useless donations, our team initially decided on transferring extra funds present in a project to other similar projects done by the NGO. 
*  To implement this option, the use of factory contract was experimented on (https://medium.com/@i6mi6/solidty-smart-contracts-design-patterns-ecfa3b1e9784).
*  These are contracts holding other contracts so that interactions and transfers between them can be done. 
*  However, after discussing with the professor and seeing how solidity is not meant for such interactions, the idea was put aside as it was considered too advanced for the purpose of this project.
