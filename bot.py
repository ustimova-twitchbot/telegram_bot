from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import socket
import os

def start(update, context):
     pass #функция для связи с сервисом получения комментариев


def error(update, context):
    update.message.reply_text('an error occured')


def text(update, context):
    text_received = update.message.text
    update.message.reply_text(f'did you said "{text_received}" ?')


def main():
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    dispatcher.add_handler(MessageHandler(Filters.text, text))

    dispatcher.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
