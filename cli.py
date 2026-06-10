import argparse

from orders import (
    place_market_order,
    place_limit_order
)

from validators import (
    validate_side,
    validate_order_type,
    validate_quantity
)


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price")

    args = parser.parse_args()

    symbol = args.symbol.upper()
    side = validate_side(args.side)
    order_type = validate_order_type(args.type)
    quantity = validate_quantity(args.quantity)

    try:

        if order_type == "MARKET":

            order = place_market_order(
                symbol,
                side,
                quantity
            )

        elif order_type == "LIMIT":

            if not args.price:
                raise ValueError(
                    "Price is required for LIMIT orders"
                )

            order = place_limit_order(
                symbol,
                side,
                quantity,
                args.price
            )

        print("\n===== ORDER SUCCESS =====")
        print(f"Order ID: {order.get('orderId')}")
        print(f"Status: {order.get('status')}")
        print(f"Symbol: {order.get('symbol')}")
        print(f"Type: {order.get('type')}")
        print(f"Side: {order.get('side')}")
        print(f"Quantity: {order.get('origQty')}")
        print(f"Executed Qty: {order.get('executedQty')}")
        print(f"Average Price: {order.get('avgPrice')}")

    except Exception as e:
        print("\n===== ORDER FAILED =====")
        print(e)


if __name__ == "__main__":
    main()