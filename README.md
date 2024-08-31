<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/io10-0x/brownie_fund_me">
    <img src="images/Logo.png" alt="Logo" width="150" height="150">
  </a>

<h3 align="center">Fund Me Smart Contract </h3>

  <p align="center">
    Smart Contract To Collect Funds (Python Version - Backend Only)

<br />
<a href="https://github.com/io10-0x/brownie_fund_me"><strong>Explore the docs »</strong></a>
<br />
<br />
<a href="https://github.com/io10-0x/brownie_fund_me">View Demo</a>
·
<a href="https://github.com/io10-0x/brownie_fund_me/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
·
<a href="https://github.com/io10-0x/brownie_fund_me/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>

  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

# About the FundMe Smart Contract

## Introduction

The FundMe smart contract is a decentralized application built using Solidity, designed to facilitate secure and transparent crowdfunding on the Ethereum blockchain. It allows users to contribute Ethereum (ETH) to the contract, tracks the amount funded by each contributor, and leverages Chainlink oracles to convert these contributions into their equivalent USD value. This ensures that all contributions meet a minimum funding threshold in USD, adding an extra layer of security and accountability.

## Key Features

- **Payment Management**: The contract is equipped to handle payments using the `payable` functions, allowing users to send ETH directly to the contract. The `msg.sender` and `msg.value` keywords are utilized to track contributions, ensuring that every transaction is securely recorded.
  
- **Owner Management**: The contract ownership is securely managed using constructors. Only the owner of the contract, designated upon deployment, has the authority to withdraw the funds. This is enforced using modifiers and the `require` keyword to ensure that only the owner's address can execute withdrawal operations.

- **Chainlink Price Feeds**: The integration with Chainlink oracles allows the contract to access real-world data, specifically the ETH/USD price. This is critical for converting Ethereum contributions into USD, ensuring that all donations meet the required minimum value in USD before they are accepted by the contract.


- **Mocking & Forking**: For local development and testing, the project includes the implementation of mock contracts using `MockV3Aggregator.sol` to simulate Chainlink price feeds. This is crucial for testing the contract's behavior in a controlled environment, ensuring consistent and reliable performance across different deployment scenarios.

## Contract Architecture

The FundMe smart contract is designed with modularity and efficiency at its core:

- **FundMe.sol**: This is the main contract responsible for managing contributions, enforcing minimum funding thresholds, and allowing the owner to withdraw funds. It interacts with Chainlink oracles to ensure accurate ETH to USD conversion.

- **MockV3Aggregator.sol**: A mock contract used during local development to simulate the behavior of Chainlink's price feeds. This allows developers to test the contract in a local environment without relying on live data, facilitating faster and more reliable development cycles.

## Deployment & Testing

The contract is deployed and tested using Brownie, a Python-based development framework that simplifies the management, deployment, and testing of smart contracts:

- **Automated Deployment**: Deployment scripts are configured to automate the process across different environments, including both local (Ganache) and testnet (e.g., Sepolia) environments. Brownie's network management capabilities ensure that the correct configurations are used for each deployment, reducing the likelihood of human error.

- **Local Development with Mocks**: During local development, the contract uses the `MockV3Aggregator` to simulate price feeds. This allows developers to test the contract's functionality without relying on live Chainlink data, making the development process faster and more efficient.

- **Comprehensive Testing**: The project includes a suite of automated tests written using Brownie's testing framework. These tests cover the core functionality of the contract, including payment handling, ownership management, and price feed integration, ensuring that the contract is reliable and bug-free before being deployed to a live environment.

## Chainlink Integration

The FundMe contract's integration with Chainlink oracles is a key feature that enhances its functionality:

- **Convert ETH to USD**: The contract uses Chainlink's decentralized oracles to fetch real-time ETH/USD prices, allowing it to accurately convert ETH contributions into USD. This ensures that all contributions meet the minimum required amount in USD, protecting both contributors and project creators.

- **Dynamic Minimum Funding Requirement**: The use of Chainlink's oracles ensures that the minimum funding threshold in USD is dynamically adjusted based on the current ETH/USD exchange rate. This provides a robust and fair mechanism for enforcing minimum contribution requirements, regardless of market fluctuations.

## Forking for Local Development

In addition to mocking, the project supports forking of live networks for local development. This allows developers to simulate a mainnet environment within their local setup, using real contract data and state from the Ethereum blockchain. Forking is particularly useful for testing interactions with live contracts without risking real funds.

For detailed setup, deployment instructions, and further information, please refer to the project's documentation and source code.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

- [![Chainlink][Chainlink.js]][Chainlink-url]
- [![OpenZeppelin][OpenZeppelin.js]][OpenZeppelin-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
# FundMe Smart Contract

## Overview

The FundMe smart contract is a Solidity-based decentralized application designed to facilitate secure crowdfunding. Users can contribute funds, and the contract ensures that only the contract owner can withdraw these funds. The contract leverages Chainlink oracles to ensure the value of contributions meets a minimum threshold in USD.

## Prerequisites

Before starting, ensure you have the following installed:

- **Python 3.6+**
- **Node.js** (includes npm)
- **VS Code** (or another preferred IDE)
- **Brownie**: Python-based development and testing framework for smart contracts

## Installation Guide

### 1. Clone the Repository

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/fundme-contract.git
cd fundme-contract
```
2. Install Required Software
2.1 Python
Download and install Python 3.6+ from python.org.
Ensure Python is added to your system’s PATH.

2.2 Node.js
Download and install Node.js from nodejs.org.
Verify the installation by running node --version and npm --version in your terminal.

2.3 Install Ganache CLI
Install Ganache CLI globally using npm:
```bash

npm install -g ganache
```
Verify the installation:
```bash
ganache --version
```

2.4 Install Yarn (Optional)
Install Yarn globally using npm:
```bash
npm install -g yarn
```

3. Set Up Environment Variables
3.1 Create a .env File
In the root directory, create a .env file (you can copy from the .env.example file provided in the repo):
```bash

cp .env.example .env
```

Update the .env file with your own credentials:
```bash

WEB3_INFURA_PROJECT_ID=your-infura-project-id
ETHERSCAN_TOKEN=your-etherscan-api-key
```
Replace your-infura-project-id and your-etherscan-api-key with your actual credentials.

4. Install Dependencies
Install the necessary dependencies using Brownie:

```bash
brownie compile
This will also install any dependencies specified in the brownie-config.yaml file, such as Chainlink contracts.
```

5. Deploying the Contract
5.1 Local Deployment (Ganache CLI)
Start Ganache CLI:
```bash
ganache
```

Deploy the contract:
```bash

brownie run scripts/deploy.py
```

5.2 Testnet Deployment (e.g., Sepolia)
Deploy to a testnet:
```bash
brownie run scripts/deploy.py --network sepolia
```

6. Verifying the Contract on Etherscan
Ensure your ETHERSCAN_TOKEN is set in the .env file.
Add publish_source=True in your deployment script.

Deploy again to auto-verify and publish:
```bash

brownie run scripts/deploy.py --network sepolia
```

7. Testing the Contract
7.1 Run Tests
Test files are located in the tests directory. Use Brownie’s built-in testing framework:

```bash

brownie test
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage
No UI is available for this contract. As a result, it can only be interacted with via etherscan after deployment on testnet/mainnet. Local interaction can only be made by developers.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/io10-0x/brownie_fund_me/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/io10-0x/brownie_fund_me/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=io10-0x/brownie_fund_me" alt="contrib.rocks image" />
</a>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

[![LinkedIn][linkedin-shield]][linkedin-url]

Project Link: [https://github.com/io10-0x/brownie_fund_me](https://github.com/io10-0x/brownie_fund_me)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

- [Smart Contract Kit Github](https://github.com/smartcontractkit/full-blockchain-solidity-course-py)
- [Blockchain and Solidity Course YT Python Version ](https://www.youtube.com/watch?v=M576WGiDBdQ)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/io10-0x/brownie_fund_me.svg?style=for-the-badge
[contributors-url]: https://github.com/io10-0x/brownie_fund_me/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/io10-0x/brownie_fund_me.svg?style=for-the-badge
[forks-url]: https://github.com/io10-0x/brownie_fund_me/network/members
[stars-shield]: https://img.shields.io/github/stars/io10-0x/brownie_fund_me.svg?style=for-the-badge
[stars-url]: https://github.com/io10-0x/brownie_fund_me/stargazers
[issues-shield]: https://img.shields.io/github/issues/io10-0x/brownie_fund_me.svg?style=for-the-badge
[issues-url]: https://github.com/io10-0x/brownie_fund_me/issues
[license-shield]: https://img.shields.io/github/license/io10-0x/brownie_fund_me.svg?style=for-the-badge
[license-url]: https://github.com/io10-0x/brownie_fund_me/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/ivan-otono-87a921261
[OpenZeppelin.js]: https://img.shields.io/badge/openzeppelin-4E5EE4?style=for-the-badge&logo=openzeppelin&logoColor=black
[OpenZeppelin-url]: https://www.openzeppelin.com/
[Chainlink.js]: https://img.shields.io/badge/chainlink-375BD2?style=for-the-badge&logo=chainlink&logoColor=black
[Chainlink-url]: https://chain.link/

