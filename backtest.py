from market_data import get_historical_data

def run_backtest():

    df = get_historical_data()

    starting_balance = 1000
    balance = starting_balance

    position = None

    trades = 0
    wins = 0
    losses = 0

    for i in range(1, len(df)):

        current_price = df["close"].iloc[i]

        previous_price = df["close"].iloc[i - 1]

        # Simple Strategy

        if previous_price < current_price and position is None:

            position = current_price

            trades += 1

        elif previous_price > current_price and position is not None:

            position_size = 0.01

            profit = (
            current_price - position
            ) * position_size

            balance += profit
            if profit > 0:
                wins += 1
            else:
                losses += 1

            position = None

    win_rate = round(
    (wins / trades) * 100,
    2
    ) if trades > 0 else 0

    return {
    "starting_balance": starting_balance,
    "final_balance": round(balance, 2),
    "profit": round(balance - starting_balance, 2),
    "trades": trades,
    "wins": wins,
    "losses": losses,
    "win_rate": win_rate
}