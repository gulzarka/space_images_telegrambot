import telegram

bot = telegram.Bot(token='5843213600:AAG-BjATLJg5n_stXWYQelOUCal8rS0CbPs')
# updates = bot.get_updates()
# chat_id = bot.get_updates()[-1].message.chat_id
# bot.send_message(chat_id='@myspaceimages', text="Hello everyone!")
bot.send_document(chat_id='@myspaceimages', document=open('nasa_images/9nasa_apod..jpg', 'rb'))