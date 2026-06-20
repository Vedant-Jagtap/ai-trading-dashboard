from charts import get_klines
from ta.momentum import RSIIndicator


def run_strategy_backtest():

    df = get_klines(
        symbol="BTCUSDT",
        interval="1h",
        limit=500
    )

    # RSI
    df["RSI"] = RSIIndicator(
        close=df["Close"],
        window=14
    ).rsi()

    # EMA
    df["EMA20"] = df["Close"].ewm(
        span=20,
        adjust=False
    ).mean()

    df["EMA50"] = df["Close"].ewm(
        span=50,
        adjust=False
    ).mean()

    # MACD
    ema12 = df["Close"].ewm(
        span=12,
        adjust=False
    ).mean()

    ema26 = df["Close"].ewm(
        span=26,
        adjust=False
    ).mean()

    df["MACD"] = ema12 - ema26

    df["MACD_SIGNAL"] = (
        df["MACD"]
        .ewm(span=9, adjust=False)
        .mean()
    )

    # Portfolio
    starting_balance = 1000
    balance = starting_balance

    position = None
    entry_price = None

    trades = 0
    wins = 0
    losses = 0

    gross_profit = 0
    gross_loss = 0

    position_size = 0.01

    # Risk Management
    stop_loss_pct = -1.0      # -1%
    take_profit_pct = 2.0     # +2%

    for i in range(50, len(df)):

        buy_score = 0
        sell_score = 0

        # RSI
        if df["RSI"].iloc[i] < 30:
            buy_score += 1
        elif df["RSI"].iloc[i] > 70:
            sell_score += 1

        # EMA
        if df["EMA20"].iloc[i] > df["EMA50"].iloc[i]:
            buy_score += 1
        else:
            sell_score += 1

        # MACD
        if df["MACD"].iloc[i] > df["MACD_SIGNAL"].iloc[i]:
            buy_score += 1
        else:
            sell_score += 1

        current_price = df["Close"].iloc[i]

        # ENTRY
        if buy_score >= 2 and position is None:

            position = "LONG"
            entry_price = current_price
            trades += 1

        # POSITION MANAGEMENT
        if position is not None:

            pct_change = (
                (current_price - entry_price)
                / entry_price
            ) * 100

            profit = (
                current_price - entry_price
            ) * position_size

            # Stop Loss
            if pct_change <= stop_loss_pct:

                balance += profit

                losses += 1
                gross_loss += profit

                position = None
                entry_price = None

            # Take Profit
            elif pct_change >= take_profit_pct:

                balance += profit

                wins += 1
                gross_profit += profit

                position = None
                entry_price = None

            # Signal Exit
            elif sell_score >= 2:

                balance += profit

                if profit > 0:
                    wins += 1
                    gross_profit += profit
                else:
                    losses += 1
                    gross_loss += profit

                position = None
                entry_price = None

    win_rate = round(
        (wins / trades) * 100,
        2
    ) if trades else 0

    profit_factor = round(
        gross_profit / abs(gross_loss),
        2
    ) if gross_loss != 0 else 0

    return {
        "starting_balance": starting_balance,
        "final_balance": round(balance, 2),
        "profit": round(balance - starting_balance, 2),
        "trades": trades,
        "wins": wins,
        "losses": losses,
        "win_rate": win_rate,
        "profit_factor": profit_factor
    }