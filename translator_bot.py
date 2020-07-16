from telebot import TeleBot
from telebot import types
from translate import Translator


class Bot:
    def __init__(self):
        self.bot = TeleBot('TOKEN')
        self.eng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
        self.rus = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
                    'у', 'ф', 'х', 'ц', 'ч', 'щ', 'ш', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        self.en_translator = Translator(to_lang="en", from_lang='ru')
        self.ru_translator = Translator(to_lang="ru", from_lang='en')

    def mess_chat(self):
        @self.bot.inline_handler(func=lambda query: len(query.query) == 0)
        def empty_query(query):
            r = types.InlineQueryResultArticle(
                id='1',
                title="Бот переводчик",
                description="Напишите слово и я переведу его для Вас",
                input_message_content=types.InputTextMessageContent(
                    message_text="Слово или фраза не введена")
            )
            self.bot.answer_inline_query(query.id, [r])

        @self.bot.inline_handler(func=lambda query: len(query.query) > 0)
        def query_text(query):
            text = str.lower(query.query)
            print('запрос слова ' + text)
            for i in range(len(self.eng)):
                if text.find(self.eng[i]) == 1:
                    translate = self.ru_translator.translate(text)
                    anc = types.InlineQueryResultArticle(
                        id='1', title="Слово/Фраза: \n '{}'".format(text),
                        description="Результат перевода:\n {}".format(translate),
                        input_message_content=types.InputTextMessageContent(
                            message_text='Слово/Фраза "{}"\n переводится как "{}"'.format(text, translate))
                    )
                    self.bot.answer_inline_query(query.id, [anc])
                elif text.find(self.rus[i]) == 1:
                    translate = self.en_translator.translate(text)
                    anc = types.InlineQueryResultArticle(
                        id='1', title="Слово/Фраза: \n '{}'".format(text),
                        description="Результат перевода:\n {}".format(translate),
                        input_message_content=types.InputTextMessageContent(
                            message_text='Слово/Фраза "{}"\n переводится как "{}"'.format(text, translate))
                    )
                    self.bot.answer_inline_query(query.id, [anc])

    def non_stop(self):
        self.bot.polling(none_stop=True)


b = Bot()
b.mess_chat(), b.non_stop()
