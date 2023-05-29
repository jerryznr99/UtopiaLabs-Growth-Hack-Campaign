import requests
from decimal import Decimal
import os
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()

address = "0xa70b638B70154EdfCbb8DbbBd04900F328F32c35"

url = "https://api.etherscan.io/api?module=account&action=txlist&address=" + address + "&apikey=" + os.getenv('yourApiKeyToken')

response = requests.get(url)

address_content = response.json()

result = address_content.get("result")

totalTxnFees = Decimal("0")

for n, transaction in enumerate(result):
    # hash = transaction.get("hash")
    # tx_from = transaction.get("from")
    # tx_to = transaction.get("to")
    # value = transaction.get("value")
    # confirmations = transaction.get("confirmations")

    gasPrice = Decimal(transaction.get("gasPrice"))
    gasPrice = Web3.from_wei(gasPrice,'ether')
    gasUsed = Decimal(transaction.get("gasUsed"))
    txnFees = gasPrice * gasUsed

    # print("Transaction ID: ", n)
    # print("hash: ", hash)
    # print("from: ", tx_from)
    # print("to: ",tx_to)
    # print("gasPrice: ", gasPrice)
    # print("gasUsed: ", gasUsed)
    # print("TxnFees: ", TxnFees)

    totalTxnFees = totalTxnFees + txnFees

print("You have spent " + str(totalTxnFees) + " in ethers")