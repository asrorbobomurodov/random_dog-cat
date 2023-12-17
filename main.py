from telegram.ext import (Dispatcher, Filters, CommandHandler, 
                          MessageHandler, CallbackContext,
                          Updater)
from settings import token
from handlers import start, cat, dog, help_command, fox, anser

def main():
    # Get the dispatcher to register handlers
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help_command))

    # on non command i.e message - send random cat or dog image on API
    dp.add_handler(MessageHandler(Filters.text('Dog 🐕'), dog))
    dp.add_handler(MessageHandler(Filters.text('Cat 🐈'), cat))
    dp.add_handler(MessageHandler(Filters.text('Fox 🦊'), fox))
    dp.add_handler(MessageHandler(Filters.all, anser))
        
    #start the bot
    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()

