from brownie import fundme, MockV3Aggregator, network, config
from scripts._helpful_scripts import getaccount, deploymock, localchain
from web3 import Web3


def deployfundme():
    account = getaccount()

    if network.show_active() not in localchain:
        pricefeed = config["networks"][network.show_active()]["ethusdpricefeed"]
    else:
        pricefeed = deploymock()

    fundmecontract = fundme.deploy(
        pricefeed,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    print(f"Contract deployed at {fundmecontract.address}")
    return fundmecontract


def main():
    deployfundme()
