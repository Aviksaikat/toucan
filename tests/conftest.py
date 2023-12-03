import pytest
import logging
import time

from ape import accounts, networks, project, Contract

@pytest.fixture
def deployer(accounts):
    yield accounts["0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B"]

@pytest.fixture
def hedgefund(deployer):
    contract = project.PepeToken.deploy(sender=deployer)
    yield contract