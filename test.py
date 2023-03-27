from web3 import Web3
from eth_abi import decode_single

# Connect to an Ethereum node
w3 = Web3(Web3.HTTPProvider('https://avalanche-fuji.infura.io/v3/ef160241ee3b4cfaa9c903ed6d33ac89'))

# Define the contract address
contract_address = '0x5BD11aFd015334Bb0E139039705Dbb395eD1175c'
# Note: replace the contract address with the address of your contract

# Define the event listener function
def handle_event(event):
    # Decode the event data using the event's signature
    signature = event['topics'][0].hex()
    if signature == '0x0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef':
        message = decode_single('(string)', bytes.fromhex(event['data'][2:])).decode('utf-8')
        print(f'MessageEvent: {message}')

# Start listening for events
event_filter = w3.eth.filter({'address': contract_address})
while True:
    events = event_filter.get_new_entries()
    for event in events:
        handle_event(event)
