from market_data import get_symbol_price

try:
    data = get_symbol_price("BTCUSDT")

    print("\n=== LIVE PRICE ===")
    print(f"Symbol: {data['symbol']}")
    print(f"Price : {data['price']}")

except Exception as e:
    print(e)