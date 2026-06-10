from charts import get_klines
from ta.momentum import RSIIndicator

def generate_signal(symbol="BTCUSDT"):

    df = get_klines(
        symbol=symbol,
        interval="1m",
        limit=100
    )

    rsi = RSIIndicator(
        close=df["Close"],
        window=14
    ).rsi()

    current_rsi = round(
        rsi.iloc[-1],
        2
    )

    if current_rsi < 30:
        signal = "BUY"
        trend = "Oversold"

    elif current_rsi > 70:
        signal = "SELL"
        trend = "Overbought"

    else:
        signal = "HOLD"
        trend = "Neutral"

    return {
    "rsi": float(current_rsi),
    "signal": signal,
    "trend": trend
}