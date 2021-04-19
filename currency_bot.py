import telebot
import requests


def get_currency(currency): # Функция для поиска валюты через API сбербанка
	currency_json = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
	if currency == 'dollar':
		result_dollar = currency_json.json()['Valute']['USD']['Value']
		res = ' Курс доллара составляет ' + str(result_dollar) + ' рублей'
		return res
	elif currency == 'euro':
		result_euro = currency_json.json()['Valute']['EUR']['Value']
		res = ' Курс евро составляет ' + str(result_euro) + ' рублей'
		return res
	else:
		currency_btc = requests.get('https://blockchain.info/ru/ticker')
		result_btc = currency_btc.json()['RUB']['buy']
		res = ' Курс биткоина составляет ' + str(result_btc) + ' рублей'
		return res


bot = telebot.TeleBot('Пропишите токен вашего бота')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('dollar', 'euro', 'bitcoin')

@bot.message_handler(commands=['start']) # Функция-приветствие при первом сообщении боту
def start_message(message):
	bot.send_message(message.chat.id, 'Привет, я подскажу тебе курсы главных валют, просто выбери интересующую тебя', reply_markup = keyboard1)

@bot.message_handler(content_types=['text']) # Обработчик текста, отправленного через кнопки в боте
def send_text(message):
	bot.send_message(message.chat.id, get_currency(message.text))

bot.polling()