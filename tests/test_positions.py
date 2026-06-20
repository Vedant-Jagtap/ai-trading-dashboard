from positions import get_open_positions

try:

    positions = get_open_positions()

    print("\n=== OPEN POSITIONS ===")

    if not positions:
        print("No Open Positions")

    for pos in positions:
        print(f"\nSymbol      : {pos['symbol']}")
        print(f"Quantity    : {pos['quantity']}")
        print(f"Entry Price : {pos['entry_price']}")
        print(f"PnL         : {pos['unrealized_pnl']}")

except Exception as e:
    print(e)