from client import get_client

client = get_client()

def get_open_positions():

    positions = client.futures_position_information()

    open_positions = []

    for position in positions:

        if float(position["positionAmt"]) != 0:

            open_positions.append({
                "symbol": position["symbol"],
                "quantity": position["positionAmt"],
                "entry_price": position["entryPrice"],
                "unrealized_pnl": position["unRealizedProfit"]
            })

    return open_positions