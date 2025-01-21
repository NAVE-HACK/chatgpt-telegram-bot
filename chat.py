import logging
from telegram.ext import Updater, CommandHandler, MessageHandler
import openai

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the ChatGPT API key and Telegram bot token
CHATGPT_API_KEY = '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'
TELEGRAM_BOT_TOKEN = '7419703060:AAEhEv7NBcSqLFCFaQ5c7EZhHAd2qKl2mBk'

# Set up the OpenAI API client
openai.api_key = CHATGPT_API_KEY

# Define a function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello! I\'m your ChatGPT-powered chatbot.')

# Define a function to handle user queries
def handle_query(update, context):
    query = update.message.text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=query,
        max_tokens=2048
    )
    context.bot.send_message(chat_id=update.effective_chat.id, text=response.choices[0].text)

# Define a main function to set up the Telegram bot
def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register the /start command handler
    dp.add_handler(CommandHandler('start', start))

    # Register the query handler
    dp.add_handler(MessageHandler(Filters.text, handle_query))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
