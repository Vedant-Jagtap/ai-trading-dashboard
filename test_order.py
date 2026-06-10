from orders import place_market_order

try:
    order = place_market_order(
        symbol="BTCUSDT",
        side="BUY",
        quantity=0.001
    )

    print("Order Placed Successfully")
    print(order)

except Exception as e:
    print("Error:", e)