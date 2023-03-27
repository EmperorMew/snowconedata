
import json
from web3 import Web3

# Replace these with the contract address and the Ethereum node provider URL
CONTRACT_ADDRESS = '0x5BD11aFd015334Bb0E139039705Dbb395eD1175c'
ETHEREUM_NODE_URL = 'https://avalanche-fuji.infura.io/v3/ef160241ee3b4cfaa9c903ed6d33ac89'

# Initialize Web3 instance
w3 = Web3(Web3.HTTPProvider(ETHEREUM_NODE_URL))

def get_past_generated_tokens_event(event_signature, from_block, to_block):
    topic0 = w3.keccak(text=event_signature).hex()
    logs = w3.eth.getLogs({
        'fromBlock': from_block,
        'toBlock': to_block,
        'address': Web3.toChecksumAddress(CONTRACT_ADDRESS),
        'topics': [topic0]
    })
    return logs

def collect_addresses():
    addresses = set()
    event_signature = 'GeneratedToken(address,uint256)'  # Replace with the correct event signature

    # Replace these with the range of blocks you want to search
    from_block = 0
    to_block = 'latest'

    logs = get_past_generated_tokens_event(event_signature, from_block, to_block)

    for log in logs:
        # Assuming the first topic (excluding the event signature) represents the address
        address = log['topics'][1]
        decoded_address = w3.eth.abi.decode_single
        ('address', Web3.toBytes(hexstr=address))
        addresses.add(decoded_address)

    return addresses

def main():
    addresses = collect_addresses()
    print(addresses)

