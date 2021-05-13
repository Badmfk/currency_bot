import telebot
import requests
from bs4 import BeautifulSoup

DOLLAR_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&oq=rehc+&aqs=chrome.1.69i57j0i10i131i433j0i10i433l2j0i10i131i433j0i10i433j0i10j0i10i131i433j0i10i433j0i10.2247j1j7&sourceid=chrome&ie=UTF-8'
ETHEREUM_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D1%8D%D1%84%D0%B8%D1%80%D0%B0&sxsrf=ALeKk03SouJkYi37DomE0nDbnNTj6HKZrQ%3A1620834840290&ei=GPqbYL-cEe7GrgT7roKYDA&oq=%D0%BA%D1%83%D1%80%D1%81+%27abhf&gs_lcp=Cgdnd3Mtd2l6EAMYATIHCCMQsQIQJzIHCCMQsQIQJzIECAAQCjIECAAQCjIKCAAQsQMQgwEQCjIKCAAQsQMQgwEQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjoHCCMQsAMQJzoHCAAQRxCwAzoHCAAQsAMQQzoECCMQJzoNCAAQhwIQsQMQgwEQFDoFCAAQsQM6CAgAELEDEIMBOgIIADoFCAAQyQM6CQgjECcQRhCCAjoHCAAQhwIQFDoGCAAQChAqOgYIABAWEB46CwgAEAoQKhBGEIICUJRNWJteYKtqaAFwAngAgAFmiAHEBpIBBDEyLjGYAQCgAQGqAQdnd3Mtd2l6yAEKwAEB&sclient=gws-wiz'
EURO_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&sxsrf=ALeKk03WCid9t0UScqSNEu-TrROEAcBJsw%3A1620835095949&ei=F_ubYLi_OeymrgSK_6aQDA&oq=%D0%BA%D1%83%D1%80%D1%81t&gs_lcp=Cgdnd3Mtd2l6EAMYADIGCAAQChAqOgcIABBHELADOgcIABCwAxBDOgUIABCxAzoECAAQQzoCCAA6BQgAEMkDOgQIIxAnOgkIIxAnEEYQggI6DAgjELACECcQRhCCAjoECAAQDToICAAQsQMQgwFQofjFAVjwk8YBYLCaxgFoBHACeACAAVGIAe4FkgECMTKYAQCgAQGqAQdnd3Mtd2l6yAEKwAEB&sclient=gws-wiz'
BITCOIN_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD%D0%B0&sxsrf=ALeKk01iaPjxXu-a4Mb0AJRqMRfXFP_BCQ%3A1620835076676&ei=BPubYNHYKMjrrgTH372QAQ&oq=%D0%BA%D1%83%D1%80%D1%81+%2Cbnrjb&gs_lcp=Cgdnd3Mtd2l6EAMYADILCAAQChAqEEYQggIyBAgAEAoyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOgcIABBHELADOgcIABCwAxBDOgQIIxAnOgUIABCxAzoCCAA6BQgAEMkDOgUIABCSAzoKCAAQhwIQsQMQFDoICAAQsQMQgwE6BAgAEEM6BwgAELEDEEM6CQgjECcQRhCCAjoNCAAQhwIQsQMQgwEQFDoHCAAQhwIQFDoGCAAQChAqUJloWMiHAWCQjgFoAXACeACAAXeIAdIFkgEEMTAuMZgBAKABAaoBB2d3cy13aXrIAQrAAQE&sclient=gws-wiz'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}


def get_currency(currency): # Функция для поиска валюты через поиск Google
	if currency == 'dollar':
		res_dollar = requests.get(DOLLAR_RUB, headers=headers)
		soup_dollar = BeautifulSoup(res_dollar.content, 'html.parser')
		res = f'Курс доллара на данный момент {soup_dollar.find_all("span", {"class": "DFlfde", "class": "SwHCTb"})[0].text} рублей'
		return res
	elif currency == 'euro':
		res_euro = requests.get(EURO_RUB, headers=headers)
		soup_euro = BeautifulSoup(res_euro.content, 'html.parser')
		res = f'Курс евро на данный момент {soup_euro.find_all("span", {"class": "DFlfde", "class": "SwHCTb"})[0].text} рублей'
		return res
	elif currency == 'bitcoin':
		res_bitcoin = requests.get(BITCOIN_RUB, headers=headers)
		soup_bitcoin = BeautifulSoup(res_bitcoin.content, 'html.parser')
		res = f'Курс биткоина на данный момент {soup_bitcoin.find_all("span", {"class": "DFlfde", "class": "SwHCTb"})[0].text} рублей'
		return res
	elif currency == 'etherium':
		res_ethereum = requests.get(ETHEREUM_RUB, headers=headers)
		soup_ethereum = BeautifulSoup(res_ethereum.content, 'html.parser')
		res = f'Курс эфира на данный момент {soup_ethereum.find_all("span", {"class": "DFlfde", "class": "SwHCTb"})[0].text} рублей'
		return res
		

bot = telebot.TeleBot('Введите свой токен')
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