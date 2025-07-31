from telegram.ext import Updater, CommandHandler
from PIL import Image
import os

# === Replace with your bot token ===
TELEGRAM_TOKEN = "YOUR_BOT_TOKEN"

def start(update, context):
    update.message.reply_text("Hello! I'm your SMC bot. Ready to send alerts!")

# Example of how to check image type using Pillow
def check_image_type(file_path):
    try:
        with Image.open(file_path) as img:
            return img.format  # e.g., 'JPEG', 'PNG'
    except Exception as e:
        return f"Error: {e}"

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
