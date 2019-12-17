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

4. __Transfer unused funds__ (This idea was then abandoned):
*  To avoid useless donations, our team initially decided on transferring extra funds present in a project to other similar projects done by the NGO. 
*  To implement this option, the use of __factory contract__ was experimented on (https://medium.com/@i6mi6/solidty-smart-contracts-design-patterns-ecfa3b1e9784).
*  These are contracts holding other contracts so that interactions and transfers between them can be done. 
*  However, after discussing with the professor and seeing how solidity is not meant for such interactions, the idea was put aside as it was considered too advanced for the purpose of this project.

5. __Provide a message to donors to avoid excess contribution__ (This is a plan B to solve the same issue as above):
*  Since we realized that the idea in point 4) was too ambitious, we decided to replace it with a `require callback` restricting donations that exceed projects' goals (that is to say: _raised funds + donation > project goal_). 
*  Nevertheless, to __inform donors__ on the exact amounts required to reach a goal, a solidity version of `string concatenation` was created to concat the missing amount value to the error message of the __require callback__. Source: https://ethereum.stackexchange.com/questions/10811/solidity-concatenate-uint-into-a-string
*  Once again, as solidity is __not__ a scripting language, this was not an easy task as values cannot be negative, only bytes can be added to each other, returning hexes, etc. 

6. __Provide payback if a project does not go through__ (the goal is not reached):
*  This function is needed to make sure that donors do not lose the money they donated if the project they wanted to fund does not go through. 
*  We decided to implement an __additional mapping__ to store and track __individual donations__. 
*  This allowed for the creation of an additional payback function of the exact donated amount (__minus the gas used to mine the block__).
* The idea is that the donor would be able to activate this function by clicking on an icon on the UI of the application __if, and only if__, the goal for the project he wanted to fund is not achieved but the deadline is passed.

7. __Utility python functions__:
*  Another problem caused by solidity being the smart contract programming language was its __lack of datetime implementation__ or __conversion possibilities__ (bad calculation capabilities). 
*  For __ease of use and understandability__ of the contract for the NGO and/or users, 2 utility functions were created in the testing notebook (`using_contract.ipynb`): 
  *  __Deadline conversion__: this function’s purpose is to transform a given deadline (expressed in __number of days__) to a deadline accessible by solidity (expressed in __block numbers__). Using the data provided here (https://medium.facilelogin.com/the-mystery-behind-block-time-63351e35603a), and simple division, we created a __loop transforming number of days into number of mined blocks__, which the contract would then see as being the deadline. The Ethereum block chain has a block mined every 10 to 19 seconds, we decided to go with 12 seconds as it was the most common number agreed upon online. 
  *  __Dollar to Wei__: Weis or even Ethers are most likely not something __potential users__ of the smart contract would be __familiar with__. So, we decided to implement a python function to retrieve the __real-time dollar value of ethers__ to __convert donation into Weis automatically__ before transferring and avoiding this difficulty for potential clients. This was done using `coinapi` with the help of the following notebook: https://notebooks.ai/santiagobasulto/coin-api-live-docs-4a628f39.
