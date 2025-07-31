import requests
from utils import get_candles, get_rsi, get_atm_strike

def check_smc_signal(symbol, interval="15m"):
    candles = get_candles(symbol, interval)
    if len(candles) < 20:
        return None

    latest = candles[-1]
    prev = candles[-2]

    bos_up = latest['high'] > max([c['high'] for c in candles[-6:-1]])
    bos_down = latest['low'] < min([c['low'] for c in candles[-6:-1]])

    rsi = get_rsi([c['close'] for c in candles])
    
    if bos_up and rsi[-1] < 30:
        strike = get_atm_strike(symbol, direction="CALL")
        return f"📈 SMC Buy Signal (BOS↑) on {symbol}\nRSI: {rsi[-1]}\n🔔 Buy Call: {strike}"
    elif bos_down and rsi[-1] > 70:
        strike = get_atm_strike(symbol, direction="PUT")
        return f"📉 SMC Sell Signal (BOS↓) on {symbol}\nRSI: {rsi[-1]}\n🔔 Buy Put: {strike}"
    
    return None
