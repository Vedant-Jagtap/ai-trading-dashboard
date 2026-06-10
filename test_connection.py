from client import get_client

client = get_client()

try:
    account = client.futures_account()
    print("✅ Connected to Binance Futures Testnet")
    print("Available Balance:", account["availableBalance"])
except Exception as e:
    print("❌ Connection Failed")
    print(e)