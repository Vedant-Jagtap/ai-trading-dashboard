from account import get_balance

try:

    balance = get_balance()

    print("\n=== ACCOUNT BALANCE ===")
    print(f"Wallet Balance    : {balance['wallet_balance']}")
    print(f"Available Balance : {balance['available_balance']}")

except Exception as e:
    print(e)