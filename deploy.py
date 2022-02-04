from brownie import accounts,config,SimpleStorage,network
  # with this account keyword we can add account in number of different ways

# Importing the contract
import os


def deploy_simple_storage():
    # account = accounts[0]  # 1.)Built in local ganache cli accounts
    # print(account)      # Spits out an address and a private key

    # if we wanna work with a test network
    # 2.) brownie accounts new freecodecamp-account   can give our own private key for testing purpose I used rinkeby faucet account-1 along with a password
    # account = accounts.load("freecodecamp-account")
    # print(account)          #Output on running
    # Enter password for "freecodecamp-account":
    # 0x11111111111111111111111111111111111
    # 3.)Environment variable and brownie config

    # account = accounts.add(os.getenv("PRIVATE_KEYS"))
    # print(account)

    # this could be further improved

    # account = accounts.add(config["wallets"]["from_key"])       #Canonocal place from where we are gonna get our key from
    # print(account)

    account = get_account()         # Based on the nature of network the account gets a ganache development account   (account[0])
                                    # or our rinkeby account is reeturned via brownie config check etherscan
    simple_storage = SimpleStorage.deploy({"from": account})  # You always need a "from" key in dictionary when making a transaction
    # This line states from whom you are deploying from
    # Gives contract obbject as output
    # print(simple_storage)
    # Brownie is smart enough to know whether its Transaction or call

    # Now recreating our web3.py in Brownie
    stored_value = (simple_storage.retrieve())  # Just a call so dont need {"from" : accountnumber}
    print(stored_value)
    transaction = simple_storage.store( 15, {"from": account})  # transaction so we are mentioning {"from": account}
    transaction.wait(1)  # wait for the transaction to complte for 1 block
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)

    # Alot more flexibility in CI/CD pipeline


def get_account():
    if(network.show_active() == "development"):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])    

def main():
    deploy_simple_storage()  # brownie compile
    # brownie run scripts/deploy.p


# In web3.py we used RPC URL/http provider through infura
