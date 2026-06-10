from client import get_client
from logging_config import logger

client = get_client()

def place_market_order(symbol, side, quantity):
    try:
        logger.info(f"MARKET Order Request: {symbol} {side} {quantity}")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logger.info(f"MARKET Order Response: {order}")

        return order

    except Exception as e:
        logger.error(f"MARKET Order Error: {str(e)}")
        raise


def place_limit_order(symbol, side, quantity, price):
    try:
        logger.info(
            f"LIMIT Order Request: {symbol} {side} {quantity} @ {price}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(f"LIMIT Order Response: {order}")

        return order

    except Exception as e:
        logger.error(f"LIMIT Order Error: {str(e)}")
        raise