from telebot import TeleBot
from config import TOKEN
from keyboards import START_KB
from models.model import Category, Product, Texts

from telebot.types import ReplyKeyboardMarkup, KeyboardButton
bot = TeleBot(token=TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    txt = Texts.objects.filter(
        text_type='Greetings'
    ).get()

    kb = ReplyKeyboardMarkup()
    buttons = [KeyboardButton(button_name) for button_name in START_KB.values()]
    kb.add(*buttons)


    bot.send_message(message.chat.id,
                     txt,
                     reply_markup=kb)