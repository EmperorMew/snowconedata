import json
from solcx import compile_standard

# Read the contract bytecode from a JSON file
with open('contract_bytecode.json', 'r') as f:
    contract_bytecode = json.load(f)['bytecode']

# Compile the contract source code to generate the ABI
contract_source = f"pragma solidity ^0.8.0; contract MyContract {{ {contract_bytecode} }}"
compiled = compile_standard(
    {
        'language': 'Solidity',
        'sources': {
            'MyContract.sol': {
                'content': contract_source,
            },
        },
        'settings': {
            'outputSelection': {
                '*': {
                    '*': ['abi'],
                },
            },
        },
    },
    allow_paths='.',
)
abi = compiled['contracts']['MyContract.sol']['MyContract']['abi']

# Write the ABI to a JSON file
with open('contract_abi.json', 'w') as f:
    json.dump(abi, f)
