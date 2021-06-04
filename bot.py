import telebot
from telebot import types
bot = telebot.TeleBot('1844271942:AAGb2uVjz4V1E3xTPwt0vKDTmbhD9dLSy0o')
@bot.message_handler (content_types= ['text'])

def start(message):
	bot.send_message(message.from_user.id, 'Привет!')
	bot.register_next_step_handler(message, get_respond)
    
@bot.message_handler(content_types=['text'])
def get_respond(message):
	bot.send_chat_action(message.from_user.id, 'typing')
	if message.text == "Привет":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		key1 = types.KeyboardButton('Gazelle City')
		key2 = types.KeyboardButton('Gazelle Next') 
		key3 = types.KeyboardButton('Gazon Next')
		key4 = types.KeyboardButton('Соболь')
		key5 = types.KeyboardButton('Валдай')
		markup.add(key1, key2, key3, key4, key5)
		bot.send_message(message.from_user.id, "Выберите модель автомобиля для конфигуратора.", reply_markup = markup)
	else:
		bot.send_message(message.from_user.id, "Напиши Привет")
bot.polling()
