from bot import TGBot
from config import TOKEN, WEBHOOK_URL, PATH
from keyboards import START_KB
from models.model import Category, Product, Cart
from flask import Flask, request, abort

from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Update
)
bot = TGBot(token=TOKEN)

app = Flask(__name__)


@app.route(f'/{PATH}', methods=['POST'])
def webhook():
    """
    Function process webhook call
    """
    if request.headers.get('content-type') == 'application/json':

        json_string = request.get_data().decode('utf-8')
        update = Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''

    else:
        abort(403)

@bot.message_handler(commands=['start'])
def start(message):
    # txt = Texts.objects.filter(
    #     text_type='Greetings'
    # ).get()
    txt = 'hello'

    kb = ReplyKeyboardMarkup()
    buttons = [KeyboardButton(button_name) for button_name in START_KB.values()]
    kb.add(*buttons)


    bot.send_message(message.chat.id,
                     txt,
                     reply_markup=kb)

@bot.message_handler(func=lambda message: message.text == START_KB['categories'])
def categories(message):
    cats = Category.objects.filter(is_root=True)

    kb = InlineKeyboardMarkup()

    buttons = [
        InlineKeyboardButton(text=cat.title, callback_data=str(cat.id)) for cat in cats
    ]

    kb.add(*buttons)
    bot.send_message(message.chat.id, text='Выберите категорию', reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'category')
def get_cat_or_products(call):
    """
    Приходит к нам id категории, получаем объект этой категории:
    1) Если объект не имеет предков - выводим продукты
    2) Если объект имеет предков выводим этих предков
    :param call:
    :return:
    """

    kb = InlineKeyboardMarkup()

    category = Category.objects.get(id=call.data.split('_'[1]))

    if category.subcategories:
        buttons = [
            InlineKeyboardButton(text=cat.title, callback_data='category_' + str(cat.id)) for cat in category.subcategories
        ]
    else:
        buttons = [
            InlineKeyboardButton(text=product.title, callback_data='product_' + str(product.id))
            for product in category.get_products()
        ]



    kb.add(*buttons)
    bot.edit_message_text(category.title, message_id=call.message.message_id,
                          chat_id=call.message.chat.id, reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'product')
def add_to_cart(call):
    cart = Cart.get_or_create_cart(user_id=call.message.chat.id)
    cart.add_product_to_cart(product_id=call.data.split('_')[1])
    bot.answer_callback_query()




"""
WEBHOOK_HOST = https://33.46.32.19:8443
PKEM = '/home/certificates/webhok_pkem.pem'
PKEY = '/home/certificates/webhook_pkey.pem'
bot.set_webhhook(WEBHOOK_HOST, open('r', PKEM))
"""

if __name__ == "__main__":
    import time
    print("STARtED")
    bot.remove_webhook()
    time.sleep(1)
    bot.set_webhook(
        url=WEBHOOK_URL,
        certificate=open('nginx-selfsigned.crt', 'r')
    )




