import json
from web3 import Web3

# Replace these with the contract ABI, contract address, and Ethereum node provider URL
TOKEN_ABI = json.loads('YOUR_ERC20_TOKEN_ABI')
CONTRACT_ADDRESS = '0x5BD11aFd015334Bb0E139039705Dbb395eD1175c'
ETHEREUM_NODE_URL = 'https://avalanche-fuji.infura.io/v3/ef160241ee3b4cfaa9c903ed6d33ac89'

# Initialize Web3 instance
w3 = Web3(Web3.HTTPProvider(ETHEREUM_NODE_URL))

# Create a token contract instance
token_contract = w3.eth.contract(address=Web3.toChecksumAddress(TOKEN_ADDRESS), abi=TOKEN_ABI)

# Fetch the total supply of tokens
total_supply = token_contract.functions.totalSupply().call()

# Replace this function with a way to iterate over all token holders
# This is just an example; you may need to customize it based on your specific token
def iterate_token_holders():
    for i in range(total_supply):
        yield token_contract.functions.holderAt(i).call()

def fetch_token_holders():
    holders = set()
    for holder in iterate_token_holders():
        holders.add(holder)
    return holders

def main():
    holders = fetch_token_holders()
    print(holders)
