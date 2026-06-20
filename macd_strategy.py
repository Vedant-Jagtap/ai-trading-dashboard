import pandas as pd
from market_data import get_klines


def get_macd_signal(symbol="BTCUSDT"):

    df = get_klines(symbol)

    # EMA 12
    ema12 = df["close"].ewm(span=12, adjust=False).mean()

    # EMA 26
    ema26 = df["close"].ewm(span=26, adjust=False).mean()

    # MACD Line
    macd = ema12 - ema26

    # Signal Line
    signal_line = macd.ewm(span=9, adjust=False).mean()

    if macd.iloc[-1] > signal_line.iloc[-1]:

        signal = "BUY"
        trend = "Bullish"

    else:

        signal = "SELL"
        trend = "Bearish"

    return {
        "macd": round(macd.iloc[-1], 2),
        "signal_line": round(signal_line.iloc[-1], 2),
        "signal": signal,
        "trend": trend
    }