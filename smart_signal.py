from signals import generate_signal
from ema_strategy import ema_signal
from macd_strategy import get_macd_signal


def smart_signal(symbol="BTCUSDT"):

    rsi_data = generate_signal(symbol)
    ema_data = ema_signal(symbol)
    macd_data = get_macd_signal(symbol)

    buy_score = 0
    sell_score = 0

    # RSI
    if rsi_data["signal"] == "BUY":
        buy_score += 1
    elif rsi_data["signal"] == "SELL":
        sell_score += 1

    # EMA
    if ema_data["signal"] == "BUY":
        buy_score += 1
    elif ema_data["signal"] == "SELL":
        sell_score += 1

    # MACD
    if macd_data["signal"] == "BUY":
        buy_score += 1
    elif macd_data["signal"] == "SELL":
        sell_score += 1

    # Final Decision
    if buy_score > sell_score:
        final_signal = "BUY"

    elif sell_score > buy_score:
        final_signal = "SELL"

    else:
        final_signal = "HOLD"

    confidence = (
        max(buy_score, sell_score) / 3
    ) * 100

    return {
        "signal": final_signal,
        "confidence": round(confidence, 2),
        "rsi": rsi_data["signal"],
        "ema": ema_data["signal"],
        "macd": macd_data["signal"]
    }