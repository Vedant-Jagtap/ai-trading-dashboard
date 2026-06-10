from signals import generate_signal
from ema_strategy import ema_signal

def smart_signal():

    rsi_data = generate_signal()
    ema_data = ema_signal()

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

    if buy_score > sell_score:
        final_signal = "BUY"

    elif sell_score > buy_score:
        final_signal = "SELL"

    else:
        final_signal = "HOLD"

    confidence = max(
        buy_score,
        sell_score
    ) / 2 * 100

    return {
        "signal": final_signal,
        "confidence": confidence,
        "rsi": rsi_data["signal"],
        "ema": ema_data["signal"]
    }