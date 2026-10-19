import os
import telebot
from telebot import types
from flask import Flask
import threading

BOT_TOKEN = "8959233284:AAFhxYO5dJysBNhgub2sZ3IaJQ9pFEq5y1Y"
ADMIN_ID = 8907869447 
UPI_ID = "rajulaldangi532@ybl"

bot = telebot.TeleBot(BOT_TOKEN)
app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "Bot is Running!"

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("📸 Insta Followers 1K - ₹70", callback_data="insta_followers"),
        types.InlineKeyboardButton("❤️ Insta Likes 1K - ₹40", callback_data="insta_likes"),
        types.InlineKeyboardButton("▶️ YT Views 1K - ₹50", callback_data="yt_views"),
        types.InlineKeyboardButton("✈️ TG Members 1K - ₹100", callback_data="tg_members")
    )
    bot.send_message(message.chat.id, "🔥 *SMM PANEL* 🔥\nService select karo:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    bot.send_message(call.message.chat.id, f"✅ {call.data}\n\nApna Link bhejo:")
    bot.register_next_step_handler(call.message, lambda m: payment_step(m, call.data))

def payment_step(message, service):
    link = message.text
    bot.send_message(message.chat.id, f"Link: {link}\n💰 UPI: {UPI_ID} pe payment karo aur screenshot bhejo.")
    try:
        bot.send_message(ADMIN_ID, f"NEW ORDER!\nUser: @{message.from_user.username}\nService: {service}\nLink: {link}")
    except: pass

def run_bot():
    print("Bot Started...")
    bot.infinity_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 10000))
    app_flask.run(host='0.0.0.0', port=port)
