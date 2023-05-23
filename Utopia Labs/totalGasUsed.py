import requests
from decimal import Decimal

YourApiKeyToken = "V6F9X1UUQIAREBV3WA3BYFHFXHIX1ZXCJK"
address = "0xa70b638B70154EdfCbb8DbbBd04900F328F32c35"

url = "https://api.etherscan.io/api?module=account&action=txlist&address=" + address + "&apikey=" + YourApiKeyToken

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

    gasPrice = transaction.get("gasPrice")
    gasPrice = Decimal(gasPrice)/Decimal("1000000000000000000")
    gasUsed = Decimal(transaction.get("gasUsed"))
    TxnFees = gasPrice * gasUsed

    # print("Transaction ID: ", n)
    # print("hash: ", hash)
    # print("from: ", tx_from)
    # print("to: ",tx_to)
    # print("gasPrice: ", gasPrice)
    # print("gasUsed: ", gasUsed)
    # print("TxnFees: ", TxnFees)

    totalTxnFees = totalTxnFees + TxnFees

print("You have spent " + str(totalTxnFees) + " in ethers")