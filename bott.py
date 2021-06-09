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
		key2 = types.KeyboardButton('Gazelle Борт') 
		key3 = types.KeyboardButton('Gazon Next')
		key4 = types.KeyboardButton('Соболь')
		key5 = types.KeyboardButton('Садко')
		markup.add(key1, key2, key3, key4, key5)
		bot.send_message(message.from_user.id, "Выберите модель автомобиля для конфигуратора.", reply_markup = markup)
		bot.register_next_step_handler(message, comp)

	else:
		bot.send_message(message.from_user.id, "Напиши Привет")

def comp(message):

	if message.text == 'Gazelle City':
		markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
		gazc1 = types.KeyboardButton('База')
        
		markup1.add(gazc1)
		bot.send_message(message.chat.id, "Выбери нужную комлектацию", reply_markup = markup1)
		bot.register_next_step_handler(message, gazc)

	elif message.text == 'Gazelle Борт':
		markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
		gazb1 = types.KeyboardButton('База')
		gazb2 = types.KeyboardButton('Комфорт + 39000₽')

		markup2.add(gazb1, gazb2)
		bot.send_message(message.chat.id, "Выбери нужную комлектацию", reply_markup = markup2)
		bot.register_next_step_handler(message, gazb)

	elif message.text == 'Gazon Next':
		markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
		gazon1 = types.KeyboardButton('База')
		gazon2 = types.KeyboardButton('Комфорт + 65700₽') 
        
		markup3.add(gazon1, gazon2)
		bot.send_message(message.chat.id, "Выбери нужную комлектацию", reply_markup = markup3)
		bot.register_next_step_handler(message, gazon)

	elif message.text == 'Соболь':
		markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
		sobol1 = types.KeyboardButton('База') 
        
		markup4.add(sobol1)
		bot.send_message(message.chat.id, "Выбери нужную комлектацию", reply_markup = markup4)
		bot.register_next_step_handler(message, sobol)

	elif message.text == 'Садко':
		markup5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
		sad1 = types.KeyboardButton('База')
		sad2 = types.KeyboardButton('Комфорт + 24000₽') 
        
		markup5.add(sad1, sad2)
		bot.send_message(message.chat.id, "Выбери нужную комлектацию", reply_markup = markup5)
		bot.register_next_step_handler(message, sad)

def gazc(message):
	if message.text == 'База':
		bot.send_message(message.chat.id, "ГУР; \nСтаблилизатор задней подвески; \nПотолочная консоль; \nУстройство ЭРА Глонасс; \nСиденье водителя с подлокотником.")
	else:
		bot.send_message(message.from_user.id, "Напиши Привет")
def gazb(message):
	if message.text == 'База':
		bot.send_message(message.chat.id, "ГУР; \nСтаблилизатор задней подвески; \nПотолочная консоль; \nУстройство ЭРА Глонасс; \nСиденье водителя с подлокотником.")
	elif message.text == 'Комфорт + 39000₽':
		bot.send_message(message.chat.id, "ГУР; \nСтаблилизатор задней подвески; \nПотолочная консоль; \nУстройство ЭРА Глонасс; \nСиденье водителя с подлокотником; \nМагнитола 2Din; \nUSB; \nЭлектропривод наружных зеркал.")

def gazon(message):
	if message.text == 'База':
		bot.send_message(message.chat.id, "Круиз контроль; \nГУР; \nABS + ASR; \nДистанционный привод КПП; \nБортовой компьютер; \nЭлектростеклоподъемнки.")
	elif message.text == 'Комфорт + 65700₽':
		bot.send_message(message.chat.id, "Круиз контроль; \nГУР; \nABS + ASR; \nДистанционный привод КПП; \nБортовой компьютер; \nЭлектростеклоподъемнки; \nВодительское сиденье 'Люкс'; \nМагнитола 2Din/USB.")

def sobol(message):
	if message.text == 'База':
		bot.send_message(message.chat.id, "ГУР; \nABS; \nСтаблилизатор задней подвески; \nПотолочная консоль; \nУстройство ЭРА Глонасс; \nСиденье водителя с подлокотником.")
	else:
		bot.send_message(message.from_user.id, "Напиши Привет")
def sad(message):
	if message.text == 'База':
		bot.send_message(message.chat.id, "ГУР; \nABS; \nЦентральный замок; \nБортовой компьютер; \nПотолочная консоль; \nnЭлектростеклоподъемнки.")
	elif message.text == 'Комфорт + 24000₽':
		bot.send_message(message.chat.id, "ГУР; \nABS; \nЦентральный замок; \nБортовой компьютер; \nПотолочная консоль; \nnЭлектростеклоподъемнки; \nДистанционный привод КПП; \nСиденье водителя с подлокотником; \nТеплопоглащающие стекла.")




bot.polling()