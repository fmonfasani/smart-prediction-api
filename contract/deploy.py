from web3 import Web3
import json
import solcx

# Conectarse a Hardhat local
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.eth.default_account = w3.eth.accounts[0]

# Compilar contrato
solcx.install_solc("0.8.0")
compiled = solcx.compile_files(["MLContract.sol"], output_values=["abi", "bin"])
contract_id, contract_interface = compiled.popitem()

# Desplegar contrato
MLContract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
tx_hash = MLContract.constructor().transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

# Guardar ABI y dirección
with open("MLContract_abi.json", "w") as f:
    json.dump(contract_interface['abi'], f)

with open("MLContract_address.txt", "w") as f:
    f.write(tx_receipt.contractAddress)

print("Contrato desplegado en:", tx_receipt.contractAddress)
