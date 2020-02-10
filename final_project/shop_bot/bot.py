from telebot import TeleBot
from models.model import Category
from telebot import types

class TGBot(TeleBot):

    def __init__(self, token, *args):
        super().__init__(token, *args)

    def root_categories(self, user_id, text, callback_lookup='category',force_send=True):
        cats = Category.objects.filter(is_root=True)

        kb = types.InlineKeyboardMarkup()

        buttons = [
            types.InlineKeyboardButton(text=cat.title, callback_data=f'{callback_lookup}_{str(cat.id)}') for cat in cats
        ]
        kb.add(*buttons)
        if not force_send:
            return kb
        self.send_message(user_id, text=text, reply_markup=kb)

    def subcategories_or_products(self,
                                  category_id,
                                  user_id=None,
                                  text=None,
                                  category_lookup='category',
                                  product_lookup='product',
                                  force_send=True):
        if not(all([user_id, text])) and force_send:
            raise Exception('Force send cannot be used without user_id or text')

        category = Category.objects.get(id=category_id)

        if category.subcategories:
            buttons = [
                types.InlineKeyboardButton(text=cat.title, callback_data=f'{category_lookup}_{cat.id}') for cat in
                category.subcategories
            ]
        else:
            buttons = [
                types.InlineKeyboardButton(text=product.title, callback_data=f'{product_lookup}_{product.id}')
                for product in category.get_products()
            ]

        kb = types.InlineKeyboardMarkup()
        kb.add(*buttons)

        if not force_send:
            return kb
        self.send_message(user_id, text, reply_markup=kb)
