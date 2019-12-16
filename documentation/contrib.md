# CONTRIBUTIONS 

### 15/11/2019
The team is formed, Federica shares the idea's material the members and a date for a first team meeting is set.

### 18/11/2019
The team meets to narrow down the idea to try and solve the problem of fraud when it comes to private donations to NGOs. 
Federica and Andrea present two relevant papers that the team should read to be up to date with the issue.

### 19/11/2019
Clara, Valentina and Federica meet to find out more on the issue of frauds in charities. Amaury and Andrea start to work to a new blockchain that could be used to solve our issue of tracking donations in an immutable way.

### 20/11/2019
The team meets since we have scheduled an office hour with the professor. Andrea and Amaury show what they have reached so far and we all try to improve on what they have written.

### 21/11/2019
The team meets to try and implement its own blockchain for this project but then, after talking with the Professor, realizes the best way to address the issue is actually to write a Solidity contract to be deployed on Ethereum. During this meeting the GitHub repository is also setup

### 22/11/2019-24/11/2019
The team members work in pairs to decide which functions to include in the smart contract and start coding it.
Initially, we think of creating two smart contracts, one for the transactions between the donor and the digital wallet and one between the wallet and the NGOs. The problem is how to make these contracts communicate. Andrea, Federica and AMaury think of implementing the first contract, Valentina and Clara think of how to structure the second one.

### 25/11/2019
The team meets with the Professor to outline an initial structure for the contract and it discusses how to solve two main issues. First, how to make the two contracts talk to each other. Second, the issue of checking whether an NGO is actually using the funds for the project it should. With regard to the former, the professor suggests using one contract to handle all transactions as having two communicating contracts would be cumbersome to implement given the recent Solidity update. With the regard to the latter, the idea of having information miners is created.

### 29/11/2019
The team meets to keep on coding the smart contract collaboratively. We have defined the main fucntions of the contract, so Amaury and Andrea work on writing the contract in Solidity, Clara, Federica and Valentina work on the PowerPoint report.

### 30/11/2019
Amaury suggests on the group chat to deploy the contract using web3, the rest of the team agrees and we start studying the relevant documentation.

### 03/12/2019
The team meets on Skype so that Amaury can show us how to implement the contract using web3. He manages to write a contract using web3 but we still have the issue of how to guarantee the validity of transactions, i.e. how to structure the role of the information miners.

### 09/12/2019
Clara, Valentina and Federica meet the Professor to discuss more into detail how to include the vote of the information miners in the contract and also how does the payback work in different situations. We then meet on Skype to update Amaury and Andrea and we discuss how to include this function in both the Solidity contract and in the Python implementation. 

### 10/12/2019-13/12/2019
The members work individually and in group on finishing the remaining tasks. Amaury and Andrea take care of completing the coding part, while Clara, Federica and Valentina work on the report and repository. We think of modifying the contract further by including a message which outputs the amount missing to reach the target for a specific project so that it is not possible to donate more than the goal for a certain project. Moreover, we take care of how to convert a deadline from number of days to number of blocks. 

### 16/12/2019
We finish to format all the deliverables, so that they can be uploaded in time for the deadline.



