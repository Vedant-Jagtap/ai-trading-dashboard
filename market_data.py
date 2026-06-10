from client import get_client

client = get_client()

def get_symbol_price(symbol):

    ticker = client.futures_symbol_ticker(
        symbol=symbol
    )

    return {
        "symbol": ticker["symbol"],
        "price": ticker["price"]
    }

def get_multiple_prices(symbols):

    prices = []

    for symbol in symbols:

        ticker = client.futures_symbol_ticker(
            symbol=symbol
        )

        prices.append({
            "symbol": symbol,
            "price": float(ticker["price"])
        })

    return prices