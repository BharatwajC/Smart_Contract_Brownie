#read from a contract we already deployed
from brownie import SimpleStorage,network,config,accounts


def read_contract():
    #print(SimpleStorage)        # Note simple storage is an array on brownie run scripts/read_value.py --network rinkeby
                                # It is goona return       <brownie.network.contract.ContractContainer object at 0x000002021C063E20>  
                                # this object gonna work same as an array
   # print(SimpleStorage[0])     #Gives us our contract address  0x8c9A367ADE7aEB697dAB0d1f1d47d9366665295e  see D:\demos\brownie_simple_storage\build\deployments\4\0x8c9A367ADE7aEB697dAB0d1f1d47d9366665295e.json

    simple_storage = SimpleStorage[-1]      #Gives us the most recent deployment  (array indexing)
    #Whenever we work with smart contract we need to know the ABI and address.Now brownie already whats the ABI and whats the Address
    #ABI when we compiled it is stored in json and Address it is stored in deployment so brownie knows it
    print(simple_storage.retrieve())        # By our last deployment output should be 15 and we got 15

def main():
    read_contract()
