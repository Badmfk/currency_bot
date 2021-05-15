import telebot
import requests
from bs4 import BeautifulSoup

DOLLAR_RUB = 'https://ru.investing.com/currencies/usd-rub'
ETHEREUM_USD = 'https://ru.investing.com/crypto/ethereum/eth-usd'
EURO_RUB = 'https://ru.investing.com/currencies/eur-rub'
BITCOIN_USD = 'https://ru.investing.com/crypto/bitcoin/btc-usd' 

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}


def get_currency(currency): 
	if currency == 'dollar':
		res_dollar = requests.get(DOLLAR_RUB, headers=headers)
		soup_dollar = BeautifulSoup(res_dollar.content, 'html.parser')
		res = f'Курс доллара на данный момент {soup_dollar.find_all("span", {"class": "arial_26", "class": "inlineblock", "class": "pid-2186-last"})[0].text} рублей'
		return res
	elif currency == 'euro':
		res_euro = requests.get(EURO_RUB, headers=headers)
		soup_euro = BeautifulSoup(res_euro.content, 'html.parser')
		res = f'Курс евро на данный момент {soup_euro.find_all("span", {"class": "arial_26", "class": "inlineblock", "class": "pid-1691-last"})[0].text} рублей'
		return res
	elif currency == 'bitcoin':
		res_bitcoin = requests.get(BITCOIN_USD, headers=headers)
		soup_bitcoin = BeautifulSoup(res_bitcoin.content, 'html.parser')
		res = f'Курс биткоина на данный момент {soup_bitcoin.find_all("span", {"class": "arial_26", "class": "inlineblock", "class": "pid-945629-last"})[0].text} долларов'
		return res
	elif currency == 'ethereum':
		res_ethereum = requests.get(ETHEREUM_USD, headers=headers)
		soup_ethereum = BeautifulSoup(res_ethereum.content, 'html.parser')
		res = f'Курс эфира на данный момент {soup_ethereum.find_all("span", {"class": "arial_26", "class": "inlineblock", "class": "pid-1058142-last"})[0].text} долларов'
		return res
		

bot = telebot.TeleBot('1560005136:AAFdwUbb40kZMMK2VspAHkzDp-gxkF40ctw')
keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard1.row('dollar', 'euro', 'bitcoin', 'ethereum')


@bot.message_handler(commands=['start']) # Функция-приветствие при первом сообщении боту
def start_message(message):
	bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}, я подскажу тебе курсы главных валют, просто выбери интересующую тебя', reply_markup = keyboard1)

@bot.message_handler(content_types=['text']) # Обработчик текста, отправленного через кнопки в боте
def send_text(message):
	if message.text == 'dollar':
		bot.send_message(message.chat.id, get_currency(message.text))
	elif message.text == 'euro':
		bot.send_message(message.chat.id, get_currency(message.text))
	elif message.text == 'bitcoin':
		bot.send_message(message.chat.id, get_currency(message.text))
	elif message.text == 'ethereum':
		bot.send_message(message.chat.id, get_currency(message.text))
	else:
		bot.send_message(message.chat.id, "Такой валюты не знаю")


bot.polling()