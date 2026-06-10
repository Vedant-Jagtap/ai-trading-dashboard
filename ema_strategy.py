from charts import get_klines

def ema_signal(symbol="BTCUSDT"):

    df = get_klines(
        symbol=symbol,
        interval="1m",
        limit=200
    )

    ema20 = df["Close"].ewm(
        span=20,
        adjust=False
    ).mean()

    ema50 = df["Close"].ewm(
        span=50,
        adjust=False
    ).mean()

    current_ema20 = round(
        float(ema20.iloc[-1]),
        2
    )

    current_ema50 = round(
        float(ema50.iloc[-1]),
        2
    )

    if current_ema20 > current_ema50:

        signal = "BUY"
        trend = "Bullish"

    elif current_ema20 < current_ema50:

        signal = "SELL"
        trend = "Bearish"

    else:

        signal = "HOLD"
        trend = "Neutral"

    return {
        "ema20": current_ema20,
        "ema50": current_ema50,
        "signal": signal,
        "trend": trend
    }   