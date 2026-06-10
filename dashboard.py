import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from charts import get_klines
from smart_signal import smart_signal
from trade_history import get_trade_history
from orders import place_market_order, place_limit_order
from market_data import get_multiple_prices
from account import get_balance
from positions import get_open_positions
from streamlit_autorefresh import st_autorefresh

st.set_page_config(
    page_title="Trading Dashboard",
    layout="wide"
)
if st.button("🔄 Refresh Dashboard"):
    st.rerun()
st_autorefresh(
    interval=10000,
    key="refresh"
)

# ====================================
# Sidebar Trading Panel
# ====================================

st.sidebar.header("Trading Panel")

symbol = st.sidebar.text_input(
    "Symbol",
    value="BTCUSDT"
)

side = st.sidebar.selectbox(
    "Side",
    ["BUY", "SELL"]
)

order_type = st.sidebar.selectbox(
    "Order Type",
    ["MARKET", "LIMIT"]
)

quantity = st.sidebar.number_input(
    "Quantity",
    min_value=0.001,
    value=0.001,
    step=0.001
)

price = None

if order_type == "LIMIT":
    price = st.sidebar.number_input(
        "Price",
        min_value=1.0,
        value=50000.0
    )

if st.sidebar.button("Place Order"):

    try:

        if order_type == "MARKET":

            order = place_market_order(
                symbol,
                side,
                quantity
            )

        else:

            order = place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        st.sidebar.success(
            f"Order Placed! ID: {order['orderId']}"
        )

    except Exception as e:
        st.sidebar.error(str(e))

# ====================================
# Main Dashboard
# ====================================

st.title("📈 Binance Futures Trading Dashboard")

# ====================================
# Live Market Prices
# ====================================

st.subheader("Live Market Prices")

symbols = [
    "BTCUSDT",
    "ETHUSDT",
    "BNBUSDT",
    "SOLUSDT"
]

prices = get_multiple_prices(symbols)

cols = st.columns(4)

for col, item in zip(cols, prices):

    with col:
        st.metric(
            item["symbol"],
            f"${item['price']:,.2f}"
        )
st.subheader("Market Chart")

chart_symbol = st.selectbox(
    "Select Symbol",
    ["BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT"]
)

interval = st.selectbox(
    "Timeframe",
    ["1m", "5m", "15m", "1h"]
)

df = get_klines(
    symbol=chart_symbol,
    interval=interval,
    limit=100
)

fig = go.Figure(
    data=[
        go.Candlestick(
            x=df["Open Time"],
            open=df["Open"],
            high=df["High"],
            low=df["Low"],
            close=df["Close"]
        )
    ]
)

fig.update_layout(
    title=f"{chart_symbol} Candlestick Chart",
    xaxis_title="Time",
    yaxis_title="Price",
    height=600
)

st.plotly_chart(
    fig,
    use_container_width=True
)
st.subheader("🤖 Smart Trading Signal")

signal_data = smart_signal()

col1, col2 = st.columns([1, 1])

# LEFT SIDE
with col1:

    signal = signal_data["signal"]

    if signal == "BUY":
        st.success(f"🟢 {signal}")

    elif signal == "SELL":
        st.error(f"🔴 {signal}")

    else:
        st.warning(f"🟡 {signal}")

# RIGHT SIDE
with col2:

    st.metric(
        "Confidence",
        f"{signal_data['confidence']}%"
    )

    st.progress(
        signal_data["confidence"] / 100
    )

st.write(f"RSI Signal : {signal_data['rsi']}")
st.write(f"EMA Signal : {signal_data['ema']}")

balance = get_balance()
st.subheader("📊 Portfolio Summary")

positions = get_open_positions()

total_pnl = 0

for pos in positions:
    total_pnl += float(
        pos["unrealized_pnl"]
    )

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Open Positions",
        len(positions)
    )

with col2:
    st.metric(
    "Total PnL",
    f"{total_pnl:.2f} USDT",
    delta=f"{total_pnl:.2f}"
)

with col3:
    st.metric(
        "Wallet Balance",
        f"{float(balance['wallet_balance']):.2f}"
    )
# ====================================
# Account Information
# ====================================

st.subheader("Account Information")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Wallet Balance",
        f"{float(balance['wallet_balance']):.2f} USDT"
    )

with col2:
    st.metric(
        "Available Balance",
        f"{float(balance['available_balance']):.2f} USDT"
    )

# ====================================
# Open Positions
# ====================================

st.subheader("Open Positions")

positions = get_open_positions()

if positions:

    df = pd.DataFrame(positions)

    df.columns = [
        "Symbol",
        "Quantity",
        "Entry Price",
        "Unrealized PnL"
    ]

    df["Unrealized PnL"] = df["Unrealized PnL"].astype(float)

    def color_pnl(val):
        if val > 0:
            return "color: lightgreen"
        elif val < 0:
            return "color: red"
        return ""

    styled_df = df.style.map(
        color_pnl,
        subset=["Unrealized PnL"]
    )

    st.dataframe(
        styled_df,
        use_container_width=True
    )

else:
    st.info("No Open Positions")

# ====================================
# Trade History
# ====================================

st.subheader("Trade History")

trade_history = get_trade_history()

if trade_history:

    history_df = pd.DataFrame(trade_history)

    st.dataframe(
        history_df,
        use_container_width=True
    )

else:
    st.info("No Trade History Available")