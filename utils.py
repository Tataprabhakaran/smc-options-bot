import requests
import numpy as np

def get_candles(symbol, interval="5m"):
    # Mocking data for now (replace with live API like TradingView or broker)
    return [
        {"open": 22000+i, "high": 22050+i, "low": 21950+i, "close": 22010+i}
        for i in range(20)
    ]

def get_rsi(close_prices, period=14):
    deltas = np.diff(close_prices)
    seed = deltas[:period]
    up = seed[seed > 0].sum() / period
    down = -seed[seed < 0].sum() / period
    rs = up / down if down else 0
    rsi = [100 - 100 / (1 + rs)]

    for delta in deltas[period:]:
        upval = max(delta, 0)
        downval = -min(delta, 0)
        up = (up * (period - 1) + upval) / period
        down = (down * (period - 1) + downval) / period
        rs = up / down if down else 0
        rsi.append(100 - 100 / (1 + rs))

    return rsi

def get_atm_strike(symbol, direction="CALL"):
    spot_price = 22000  # Replace with live price
    atm = round(spot_price / 50) * 50
    return f"{symbol} {atm} {direction}"
