# AI-Powered Binance Futures Trading Dashboard

## Overview

The AI-Powered Binance Futures Trading Dashboard is a Python-based trading analytics platform built using Binance Futures Testnet APIs and Streamlit. The project enables users to monitor live cryptocurrency market data, execute simulated futures trades, analyze technical indicators, generate trading signals, and evaluate strategy performance through historical backtesting.

The primary objective of this project was to understand how algorithmic trading systems are designed, how technical indicators can be combined into decision-making engines, and how trading strategies can be evaluated using quantitative performance metrics.

---

## Features

### Live Trading Dashboard

* Real-time cryptocurrency price monitoring
* Interactive Streamlit dashboard
* Portfolio and account balance tracking
* Open positions monitoring
* Order placement interface

### Binance Futures Integration

* Secure API authentication
* Market Order execution
* Limit Order execution
* Account information retrieval
* Position management

### Technical Analysis

The dashboard implements multiple technical indicators:

#### RSI (Relative Strength Index)

* Detects overbought and oversold conditions
* Generates BUY, SELL, and HOLD signals

#### EMA (Exponential Moving Average)

* EMA20 and EMA50 crossover analysis
* Trend identification

#### MACD (Moving Average Convergence Divergence)

* Momentum analysis
* Trend reversal detection

### Smart Signal Engine

A custom signal engine combines multiple indicators:

RSI + EMA + MACD → BUY / SELL / HOLD

This reduces reliance on a single indicator and provides more robust trading decisions.

### Historical Backtesting

The project includes a strategy backtesting module that evaluates trading strategies on historical Binance Futures data.

Features:

* Historical data retrieval
* Trade simulation
* Profit and loss calculation
* Strategy performance evaluation

### Risk Management

Implemented risk controls include:

* Stop Loss
* Take Profit
* Position sizing logic

### Performance Analytics

The strategy evaluation module calculates:

* Net Profit
* Total Trades
* Winning Trades
* Losing Trades
* Win Rate
* Profit Factor
* Maximum Drawdown
* Sharpe Ratio

---

## Technology Stack

### Programming Language

* Python

### Libraries & Frameworks

* Streamlit
* Pandas
* NumPy
* TA (Technical Analysis Library)
* Python Binance SDK
* python-dotenv

### APIs

* Binance Futures Testnet API

---

## Project Architecture

Binance Futures API
↓
Market Data Retrieval
↓
Technical Indicators
(RSI, EMA, MACD)
↓
Smart Signal Engine
↓
Trading Dashboard
↓
Backtesting Engine
↓
Performance Analytics

---

## Backtesting Results

Latest Strategy Metrics:

* Profit: +4.89 USDT
* Win Rate: 36.36%
* Profit Factor: 1.08
* Maximum Drawdown: 3.18%
* Sharpe Ratio: 0.04

These results demonstrate a complete workflow for evaluating trading strategies using historical data and risk-adjusted performance metrics.

---

## Learning Outcomes

Through this project, I gained practical experience in:

* Financial market data analysis
* Binance API integration
* Algorithmic trading concepts
* Technical indicator implementation
* Quantitative strategy evaluation
* Risk management techniques
* Streamlit dashboard development
* Python project architecture

---

## Future Improvements

Potential future enhancements include:

* Machine Learning based signal prediction
* Multi-asset portfolio management
* Advanced strategy optimization
* Trade journaling system
* Cloud deployment
* Automated trading execution

---

## Disclaimer

This project is built for educational and research purposes using Binance Futures Testnet. It is not intended to provide financial advice or guarantee trading profitability.
