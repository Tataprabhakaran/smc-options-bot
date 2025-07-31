from smc_engine import check_smc_signal
from telegram_bot import send_telegram_alert
import os

def handler():
    signal = check_smc_signal("NIFTY", interval="5m")
    if signal:
        send_telegram_alert(signal)

if __name__ == "__main__":
    handler()
