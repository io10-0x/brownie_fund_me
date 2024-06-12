from scripts._helpful_scripts import getaccount
from brownie import fundme
from scripts.deploy import deployfundme


def fund():
    fund_me = fundme[-1]
    account = getaccount()
    entrance_fee = fund_me.getentrancefee()
    print(f"The entrance fee is {entrance_fee}")
    print("Funding....")
    timetofund = fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = fundme[-1]
    account = getaccount()
    fund_me.withdraw({"from": account})


def main():
    fund()
