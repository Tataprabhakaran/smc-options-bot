from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I'm your SMC bot. Ready to send alerts!")

# Error handler
def error(update: Update, context: CallbackContext) -> None:
    logger.warning(f"Update {update} caused error {context.error}")

def main():
    """Start the bot."""
    # Get your bot token from BotFather
    TELEGRAM_TOKEN = "YOUR_BOT_TOKEN"  # Replace with your bot's token

    # Create Updater and pass it your bot's token.
    updater = Updater(TELEGRAM_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handler for /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Log all errors
    dispatcher.add_error_handler(error)

    # Start polling for updates
    updater.start_polling()

    # Block until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()
