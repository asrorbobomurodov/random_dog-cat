from telegram import Update
from cat_dog import get_cat, get_dog, get_fox
from keyboards import start_keyboard
from telegram.ext import CallbackContext

def start(update:Update, context: CallbackContext):
    user = update.effective_user
    update.message.reply_markdown_v2(fr'Hi {user.mention_markdown_v2()}\!', 
                              reply_markup=start_keyboard)

def help_command(update: Update, context: CallbackContext):
    update.message.reply_html("<b> Please click: </b> 'Dog 🐕' or 'Cat 🐈' keyboard button")

def dog(update: Update, context: CallbackContext):
    """send random dog picture"""
    update.message.reply_photo(get_dog(), caption="<b><i>Dog picture</i></b>", parse_mode='HTML')

def cat(update: Update, context: CallbackContext):
    """send random cat picture"""
    update.message.reply_photo(get_cat())

def fox(update: Update, context: CallbackContext):
    '''send a random fox image'''
    update.message.reply_photo(get_fox(), caption='My name is Fox')

def anser(update: Update, context: CallbackContext):
    '''reply message for all another msgs'''
    update.message.reply_text("Click /help!")