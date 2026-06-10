from client import get_client

client = get_client()

def get_balance():

    account = client.futures_account()

    return {
        "wallet_balance": account["totalWalletBalance"],
        "available_balance": account["availableBalance"]
    }