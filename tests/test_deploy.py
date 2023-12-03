import pytest
from ape import networks, Contract, accounts
import time
import logging

def test_deploy(deployer, hedgefund):
    assert hedgefund.balanceOf(deployer.address) > 0