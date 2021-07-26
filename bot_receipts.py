import telebot
import config_bot_receipts
import bd_receipt

bot = telebot.TeleBot(config_bot_receipts.TG_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	if message.from_user.id == config_bot_receipts.CHAT_ID_I:
		bot.reply_to(message, bd_receipt.start_text)
	elif message.from_user.id == config_bot_receipts.CHAT_ID_A:
		bot.reply_to(message, bd_receipt.start_text)
	else:
		bot.send_message(message.chat.id, "It's just test")

@bot.message_handler(content_types=['text'])
def text_message(message):
	if message.from_user.id == config_bot_receipts.CHAT_ID_I:
		for numbers, values in bd_receipt.bd.items():
			if message.text == numbers:
				bot.reply_to(message, f'{values["Name"]}\n{values["Description"]}\n{values["Rec"]}\nC/c - {values["CC"]}\nPrice - {values["Price"]}\nCustomer - {values["Customer"]}')
				bot.send_message(message.chat.id, bd_receipt.start_text)
	elif message.from_user.id == config_bot_receipts.CHAT_ID_A:
		for numbers, values in bd_receipt.bd.items():
			if message.text == numbers:
				bot.reply_to(message, f'{values["Name"]}\n{values["Description"]}\nC/c - {values["CC"]}\nPrice - {values["Price"]}\nCustomer - {values["Customer"]}')
				bot.send_message(message.chat.id, bd_receipt.start_text)

if __name__ == "__main__":
	bot.polling(none_stop=True)