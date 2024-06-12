from scripts._helpful_scripts import getaccount, localchain
from scripts.deploy import deployfundme
from brownie import network, accounts
import pytest


def test_thefundandwithdraw():
    print(f"Active network before connecting: {network.show_active()}")
    account = getaccount()
    fund_me = deployfundme()
    entrance_fee = fund_me.getentrancefee() + 100
    timetofund = fund_me.fund({"from": account, "value": entrance_fee})
    timetofund.wait(1)
    assert fund_me.addresstoval(account.address) == entrance_fee
    timetowithdraw = fund_me.withdraw({"from": account})
    timetowithdraw.wait(1)
    assert fund_me.addresstoval(account.address) == 0


def test_onlyowner():
    if network.show_active() not in localchain:
        pytest.skip()
    fund_me = deployfundme()
    bad_actor = accounts.add()
