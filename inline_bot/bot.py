from telebot import TeleBot
from telebot import types
token = "1002650340:AAEe08FO5pKUCdtaq50F-xNSwJeVKN0JXQE"
bot = TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    kb = types.InlineKeyboardMarkup()

    kb.add(
        types.InlineKeyboardButton(text='dadsa',
                                   switch_inline_query_current_chat='dasdsa???',
                                   )
    )

    bot.send_message(message.chat.id, 'da', reply_markup=kb)


@bot.inline_handler(func=lambda query: True)
def empty_query(query):

    print(query)
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text='a', callback_data='??'))
    hint = "Введите ровно 2 числа и получите результат!"
    try:
        print("inline_handler " + str(query))
        r = types.InlineQueryResultArticle(
                thumb_url='https://images.pexels.com/photos/414612/pexels-photo-414612.jpeg',
                id='1',
                title="Бот \"Математика\"",
                input_message_content=types.InputTextMessageContent(
                    message_text='THIS IS TEXT'

                ),
                reply_markup=kb,
                description=hint,
        )
        bot.answer_inline_query(query.id, [r])
    except Exception as e:
        print(e)


@bot.callback_query_handler(lambda call: True)
def s(call):
    print(call)

@bot.chosen_inline_handler(func=lambda chosen_inline_result: True)
def test_chosen(chosen_inline_result):
    print(chosen_inline_result)


bot.polling()
