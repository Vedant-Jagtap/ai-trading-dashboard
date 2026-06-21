from client import get_client
import pandas as pd

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


def get_klines(
    symbol="BTCUSDT",
    interval="1m",
    limit=100
):

    klines = client.futures_klines(
        symbol=symbol,
        interval=interval,
        limit=limit
    )

    df = pd.DataFrame(
        klines,
        columns=[
            "open_time",
            "open",
            "high",
            "low",
            "close",
            "volume",
            "close_time",
            "quote_asset_volume",
            "number_of_trades",
            "taker_buy_base",
            "taker_buy_quote",
            "ignore"
        ]
    )

    df["open"] = df["open"].astype(float)
    df["high"] = df["high"].astype(float)
    df["low"] = df["low"].astype(float)
    df["close"] = df["close"].astype(float)
    df["volume"] = df["volume"].astype(float)

    return df


def get_historical_data(
    symbol="BTCUSDT",
    interval="1h",
    limit=500
):

    return get_klines(
        symbol=symbol,
        interval=interval,
        limit=limit
    )