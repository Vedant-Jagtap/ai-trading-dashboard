# Binance Futures Testnet Trading Bot

## Overview

A Python-based trading bot that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).

## Features

- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- Command-line interface using argparse
- Input validation
- Logging of requests, responses, and errors
- Exception handling

## Project Structure

```
trading_bot/
│
├── client.py
├── orders.py
├── validators.py
├── logging_config.py
├── cli.py
├── .env
├── requirements.txt
├── README.md
└── logs/
```

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file:

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

## Usage

### MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

## Logging

Logs are stored in:

```
logs/trading.log
```

## Assumptions

- Binance Futures Testnet is used.
- User provides valid API credentials.
- Quantity and symbol comply with Binance rules.