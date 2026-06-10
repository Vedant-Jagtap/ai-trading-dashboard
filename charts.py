from client import get_client
import pandas as pd

client = get_client()

def get_klines(symbol="BTCUSDT", interval="1m", limit=100):

    klines = client.futures_klines(
        symbol=symbol,
        interval=interval,
        limit=limit
    )

    df = pd.DataFrame(
        klines,
        columns=[
            "Open Time",
            "Open",
            "High",
            "Low",
            "Close",
            "Volume",
            "Close Time",
            "Quote Asset Volume",
            "Number of Trades",
            "Taker Buy Base",
            "Taker Buy Quote",
            "Ignore"
        ]
    )

    df["Open"] = df["Open"].astype(float)
    df["High"] = df["High"].astype(float)
    df["Low"] = df["Low"].astype(float)
    df["Close"] = df["Close"].astype(float)

    df["Open Time"] = pd.to_datetime(
        df["Open Time"],
        unit="ms"
    )

    return df
