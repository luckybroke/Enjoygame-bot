from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Replace with your bot token
BOT_TOKEN = 7798123568:AAFAz1WLc81wdcluQKIG WAJK1MgbiUd49pM

# Replace with your channels (without https://t.me/)
REQUIRED_CHANNELS = ["brokeharry", "hots_games"]

GAMES = {
    "Tic Tac Toe 🎯": "https://tictactoe.iceiy.com",
    "3D Car Game 🚗": "https://cargame3d.iceiy.com",
    "Fruit Slice 🍉": "https://fruitslice.iceiy.com"
}


def start(update: Update, context: CallbackContext):
    user = update.effective_user
    chat_id = update.effective_chat.id

    # Check if user is member of required channels
    not_joined = []
    for channel in REQUIRED_CHANNELS:
        try:
            member = context.bot.get_chat_member(f"@{channel}", user.id)
            if member.status not in ['member', 'administrator', 'creator']:
                not_joined.append(channel)
        except:
            not_joined.append(channel)

    if not_joined:
        text = "❗To play games, please join these channels first:"
        buttons = [[InlineKeyboardButton(f"Join @{ch}", url=f"https://t.me/{ch}")] for ch in not_joined]
        buttons.append([InlineKeyboardButton("✅ I've Joined", callback_data="check_membership")])
        update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(buttons))
    else:
        show_games(update, context)