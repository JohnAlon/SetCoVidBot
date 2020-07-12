from config import TOKEN
from telebot import types
from covid import Covid
import telebot
import pydantic
import requests

covid = Covid()
covid.get_data()

ukr = covid.get_status_by_country_name("ukraine")
rus = covid.get_status_by_country_name("russia")
bel = covid.get_status_by_country_name("belarus")
uni = covid.get_status_by_country_name("us")

# Token
bot = telebot.TeleBot(TOKEN)

# Keyboard
def keyboard():
	markup = types.ReplyKeyboardMarkup()
	btn_wrld = types.KeyboardButton("🌎 World")
	btn_uk = types.KeyboardButton("🇺🇦 Ukraine")
	btn_ru = types.KeyboardButton("🇷🇺 Russia")
	btn_bl = types.KeyboardButton("🇧🇾 Belarus")
	btn_usa = types.KeyboardButton("🇺🇸 USA")
	markup.add(btn_wrld,btn_uk,btn_ru,btn_bl,btn_usa)
	return markup

# Bot
@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, "<b>CoVid19 Bot</b>\nThis bot monitors coronavirus statistics.",
	parse_mode='HTML', reply_markup=keyboard())

@bot.message_handler(content_types=['text'])
def country(message):
	if message.text == '🌎 World':
			bot.send_message(message.chat.id, "<b>World statistics:</b>\n" +
			"<em>Confirmed cases:</em>" + str(covid.get_total_confirmed_cases()) + "\n" + 
			"<em>Active cases:</em>" + str(covid.get_total_active_cases()) + "\n" + 
			"<em>Recovered:</em>" + str(covid.get_total_recovered()) + "\n" + 
			"<em>Deaths:</em>" + str(covid.get_total_deaths()), parse_mode='HTML')

	elif message.text == '🇺🇦 Ukraine':
			bot.send_message(message.chat.id, "<b>Ukraine statistics:</b>\n" +
			"<em>Confirmed cases:</em>" + str(ukr['confirmed']) + "\n" +
			"<em>Active cases:</em>" + str(ukr['active']) + "\n" +
			"<em>Recovered:</em>" + str(ukr['recovered']) + "\n" +
			"<em>Deaths:</em>" + str(ukr['deaths']),
			parse_mode='HTML')

	elif message.text == '🇷🇺 Russia':
			bot.send_message(message.chat.id, "<b>Russia statistics:</b>\n" +
			"<em>Confirmed cases:</em>" + str(rus['confirmed']) + "\n" +
			"<em>Active cases:</em>" + str(rus['active']) + "\n" +
			"<em>Recovered:</em>" + str(rus['recovered']) + "\n" +
			"<em>Deaths:</em>" + str(rus['deaths']),
			parse_mode='HTML')

	elif message.text == '🇧🇾 Belarus':
			bot.send_message(message.chat.id, "<b>Belarus statistics:</b>\n" +
			"<em>Confirmed cases:</em>" + str(bel['confirmed']) + "\n" +
			"<em>Active cases:</em>" + str(bel['active']) + "\n" +
			"<em>Recovered:</em>" + str(bel['recovered']) + "\n" +
			"<em>Deaths:</em>" + str(bel['deaths']),
			parse_mode='HTML')

	elif message.text == '🇺🇸 USA':
			bot.send_message(message.chat.id, "<b>USA statistics:</b>\n" +
			"<em>Confirmed cases:</em>" + str(uni['confirmed']) + "\n" +
			"<em>Active cases:</em>" + str(uni['active']) + "\n" +
			"<em>Recovered:</em>" + str(uni['recovered']) + "\n" +
			"<em>Deaths:</em>" + str(uni['deaths']),
			parse_mode='HTML')						


	
# Polling
bot.polling(none_stop=True)