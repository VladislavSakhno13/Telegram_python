import telebot
import config
import requests
from telebot import types
bot = telebot.TeleBot(config.TOKEN)
def get_ETH_cost():
    cost_ETH = requests.get("https://api.binance.com/api/v1/klines?symbol=ETHUSDT&interval=1m&limit=1")
    return float(cost_ETH.json()[0][4])
def get_BTC_cost():
    cost_BTC = requests.get("https://api.binance.com/api/v1/klines?symbol=BTCUSDT&interval=1m&limit=1")
    return float(cost_BTC.json()[0][4])
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в check bot, Введите команду /info для получения информации по представленным криптовалютам. Так же введите желаему цену, что бы бот сообщил вам, когда цена будет достигнута.')
@bot.message_handler(commands=['info'])
def start_message(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_info_ETH = types.InlineKeyboardButton(text='получить цену ETH',callback_data='info_ETH')
    item_info_BTC = types.InlineKeyboardButton(text='получить цену BTC', callback_data='info_BTC')
    markup_inline.add(item_info_ETH,item_info_BTC)
    bot.send_message(message.chat.id, 'Добро пожаловать в check bot, выберите криптовалюту по которой хотите получить цену',reply_markup=markup_inline)
@bot.callback_query_handler(func=lambda call:True)
def send_cost(call):
    if call.data == 'info_ETH':
        bot.send_message(call.message.chat.id,get_ETH_cost())
    elif call.data == 'info_BTC':
        bot.send_message(call.message.chat.id,get_BTC_cost())



@bot.message_handler(content_types=['text'])
def send_text(message):
    try:

            get_message = float(message.text)
            while_bool = True
            while while_bool:
                Get_API_BIN = get_ETH_cost()
                if (Get_API_BIN == get_message):
                    # print(get_ETH_cost())
                    bot.send_message(message.chat.id,get_ETH_cost())
                    while_bool = False
    except ValueError:
        bot.send_message(message.chat.id, 'ты придурка за меня не держи')
    except ConnectionError:
        bot.send_message(message.chat.id, 'Какие то технические шоколадки. Все равно зайди на бинанс глянь как там дела обстоят.')
bot.polling()
