from telegram.ext import Updater, CommandHandler
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not found. Set it in Render Environment Variables.")

def start(update, context):
    update.message.reply_text("SMC Bot is running!")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    print("Bot started... polling.")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
