from telegram import Update, ReplyKeyboardMarkup, KeyboardButton

start_keyboard = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text='Dog 🐕'), KeyboardButton(text='Cat 🐈')],
        [KeyboardButton(text='Fox 🦊')]
    ],
    resize_keyboard=True
)