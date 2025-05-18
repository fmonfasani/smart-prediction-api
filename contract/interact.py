from solcx import compile_source
from web3 import Web3
import json
import os   

# Setup básico de Web3
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))  # cambiar a tu red

# Cargar ABI
with open("contract/MLContract.sol", "r") as file:
    contract_source_code = file.read()

compiled_sol = compile_source(contract_source_code)
contract_id, contract_interface = compiled_sol.popitem()
abi = contract_interface['abi']

# Dirección del contrato ya desplegado
contract_address = Web3.to_checksum_address("0x...")  # ← tu dirección aquí

# Crear instancia del contrato
contract = w3.eth.contract(address=contract_address, abi=abi)

def send_prediction_to_contract(prediction: int):
    account = w3.eth.accounts[0]
    tx_hash = contract.functions.recordPrediction(prediction).transact({'from': account})
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return receipt
