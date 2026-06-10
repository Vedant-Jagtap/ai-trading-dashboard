import re

def get_trade_history(log_file="logs/trading.log"):

    trades = []

    try:
        with open(log_file, "r") as file:

            for line in file:

                if "Order Request" in line:

                    timestamp = line.split(" - ")[0]

                    match = re.search(
                        r'(MARKET|LIMIT) Order Request: (\w+) (BUY|SELL) ([0-9.]+)',
                        line
                    )

                    if match:

                        order_type = match.group(1)
                        symbol = match.group(2)
                        side = match.group(3)
                        quantity = match.group(4)

                        trades.append({
                            "Time": timestamp,
                            "Symbol": symbol,
                            "Side": side,
                            "Type": order_type,
                            "Quantity": quantity
                        })

        return trades

    except Exception:
        return []