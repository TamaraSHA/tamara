import telebot

bot = telebot.TeleBot('1844271942:AAGb2uVjz4V1E3xTPwt0vKDTmbhD9dLSy0o')
@bot.message_handler (content_types= ['text'])

def start(message):
	bot.send_message(message.from_user.id, 'Привет!')
	bot.register_next_step_handler(message, get_respond)

def get_respond(message):
	bot.send_chat_action(message.from_user.id, 'typing')
	if message.text == "Привет":
		bot.seng_message(message.from_user.id, "Добрый день! Выберите модель автомобиля для конфигуратора.")
	else:
		bot.send_message(message.from_user.id, "Напиши Привет")
bot.polling()
