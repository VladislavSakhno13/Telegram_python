import telebot
import config
import requests
bot = telebot.TeleBot(config.TOKEN)
def get_ETH_cost():
    cost_ETH = requests.get("https://api.binance.com/api/v1/klines?symbol=ETHUSDT&interval=1m&limit=1")
    return float(cost_ETH.json()[0][4])
@bot.message_handler(content_types=['text'])
def send_text(message):
    print("Ваша цена-"+str(message.text))
    print("Текущая цена-"+str(get_ETH_cost()))
    while_bool = True
    while while_bool:
        Get_API_BIN = get_ETH_cost()
        if (Get_API_BIN == float(message.text)):
            #print(get_ETH_cost())
            bot.send_message(message.chat.id, get_ETH_cost())
            while_bool = False

bot.polling()
