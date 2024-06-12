from brownie import accounts, MockV3Aggregator, config, network
import web3

localchain = ["development", "ganacheui2", "ganacheui3"]
forkedchains = ["mainnet-fork-dev"]


def deploymock():
    account = accounts[0]
    print(f"The active network is {network.show_active()}")
    print("Deploying mock...")
    mockv3contract = MockV3Aggregator.deploy(8, 200000000000, {"from": account})
    return mockv3contract.address


def getaccount():
    if network.show_active() in localchain or network.show_active() in forkedchains:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
