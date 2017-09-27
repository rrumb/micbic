from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start (bot, update):
    upate.message.reply_text('mic bic!!')

def hello (bot, update):
    update.message.reply_text('hey, {}'.format(update.message.from_user.first_name))

def echo (bot, update):
    update.message.reply_text(update.message.text)




def main():
    updater = Updater('')

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('hello', hello))
    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()


