import telebot

# अपना Telegram Bot Token यहाँ डालो
TOKEN = "7912607876:AAGia0GY6niFfi023XRbnriEhbwlb5RD8bM"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, "Hello! मैं ज़ारा AI हूँ। तुम मुझसे कुछ भी बात कर सकते हो। 😉")

print("🤖 Bot is running...")
bot.polling()
