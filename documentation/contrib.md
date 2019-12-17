# CONTRIBUTIONS 

### 15/11/2019
The __team__ is formed, __Federica__ shares the idea's material with the team members and a date for a first team meeting is set.

### 18/11/2019
The __team__ meets to narrow down the idea to try and solve the problem of fraud when it comes to private donations to NGOs. 
__Federica__ and __Andrea__ present two relevant papers that the team should read to be up to date with the issue.

### 19/11/2019
__Clara__, __Valentina__ and __Federica__ meet to find out more on the issue of frauds in charities. __Amaury__ and __Andrea__ start to work on a new blockchain that could be used to solve our issue of tracking donations in an immutable way.

### 20/11/2019
The __team__ meets since there is scheduled an office hour with the __Professor__. __Andrea__ and __Amaury__ show what they have reached so far and all the team members work collaboratively to expand what they have written.

### 21/11/2019
The __team__ meets with the idea of continuing with the implementation of its own blockchain but then, after talking with the __Professor__, it realizes that the best way to address the issue is actually to write a Solidity contract to be deployed on Ethereum. During this meeting the GitHub repository is also setup.

### 22/11/2019-24/11/2019
The team members work in groups to decide which functions to include in the smart contract/s and then start coding it/them.
Initially, the idea is to create two smart contracts, one for the transactions between the donor and the digital wallet and one between the digital wallet and the NGOs. The problem is how to make these contracts communicate. __Andrea__, __Federica__ and __Amaury__ are reposible for implementing the first contract, __Valentina__ and __Clara__ are responsible for the second one.

### 25/11/2019
The __team__ meets with the __Professor__ to outline an initial structure for the contract/s and it discusses how to solve two main issues. Firstly, how to make two contracts talk to each other. Secondly, how to check whether an NGO is actually using the funds for the project it should. With regards to the former, the Professor suggests using a single contract to handle all transactions as having two communicating contracts would be cumbersome to implement given the recent Solidity update. With regards to the latter, the idea of having information miners is created (for more details on information miners please refer to the pdf presentation).

### 29/11/2019
The __team__ meets to keep on coding the smart contract collaboratively. We have defined the main fucntions of the contract, so __Amaury__ and __Andrea__ work on writing the contract in Solidity. In the mean time __Clara__, __Federica__ and __Valentina__ work on the PowerPoint report.

### 30/11/2019
As we have seen in class, the __team__ decides to try and deploy the contract using web3 so all the members meet to study together the relevant documentation and a Jupyter Notebook is set up to try and use the contract.

### 03/12/2019
The __team__ meets on Skype and __Amaury__ helps the team to fix some issues that were encountered while deploying the contract using web3. Thanks to this call, the team is able to deploy the contract using web3. At this point, the remaining issue is how to guarantee the validity of transactions, i.e. how to structure the role of the information miners.

### 09/12/2019
__Clara__, __Valentina__ and __Federica__ meet with the __Professor__ to discuss more into detail how to include the vote of the information miners in the contract and the way in which the payback function should work in different situations. The team then meets again on Skype to update __Amaury__ and __Andrea__ and we discuss how to include this function in both the Solidity contract and in the Python implementation. 

### 10/12/2019-13/12/2019
The members work individually and in group on finishing the remaining tasks. __Amaury__ and __Andrea__ take care of completing the coding part (Solidity contract and Python implementation). __Clara__ and __Federica__ focus on the presentation and __Valentina__ manages and organizes the files on the repository. Moreover, the __team__ comes up with the idea of modifying the contract further by including a message which outputs the amount missing to reach the target for a specific project so that it is not possible to donate more than the goal. Finally, the team takes care of how to convert a deadline from number of days to number of blocks. 

### 16/12/2019
The __team__ finishes to format all the deliverables, so that they can be uploaded in time for the deadline.
