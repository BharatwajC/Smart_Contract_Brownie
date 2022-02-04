from brownie import SimpleStorage, accounts
import os


def test_deploy():
    # Arrange
    account = accounts[0]

    # Act
    simple_storage = SimpleStorage.deploy(
        {"from": account}
    )  # Same as our deploy we are deploying
    starting_value = simple_storage.retrieve()
    expected = 0

    # Assert
    assert starting_value == expected  # We can test this by using brownie test


def test_update_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy(
        {"from": account}
    )  # As we are just deploying and it is just part of the setup
    # Act
    expected = 15
    simple_storage.store(
        expected, {"from": account}
    )  # storing expected in the simplestorage.store() - transaction so we use {"from":accountno}
    # Assert
    assert expected == simple_storage.retrieve()


# Some useful flags in test

# brownie test -k test_update_storage  -  to test particular function


# brownie test --pdb   - used for trouble shooting  it goes to python

# brownie test -s  - Little robust and i guess


# CHECK OUT pytest documentation
