import telebot
from telebot import types

BOT_TOKEN = "8959233284:AAFhxYO5dJysBNhgub2sZ3IaJQ9pFEq5y1Y"
ADMIN_ID = 8907869447 
UPI_ID = "rajulaldangi532@ybl"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("📸 Instagram Followers 1K - ₹70", callback_data="insta_followers"),
        types.InlineKeyboardButton("❤️ Instagram Likes 1K - ₹40", callback_data="insta_likes"),
        types.InlineKeyboardButton("▶️ YouTube Views 1K - ₹50", callback_data="yt_views"),
        types.InlineKeyboardButton("✈️ Telegram Members 1K - ₹100", callback_data="tg_members")
    )
    bot.send_message(message.chat.id, "🔥 *SMM PANEL* 🔥\nService select karo:", reply_markup=markup, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    service_map = {
        "insta_followers": "Instagram Followers 1K - ₹70",
        "insta_likes": "Instagram Likes 1K - ₹40",
        "yt_views": "YouTube Views 1K - ₹50",
        "tg_members": "Telegram Members 1K - ₹100"
    }
    bot.send_message(call.message.chat.id, f"✅ {service_map[call.data]}\n\nApna Link bhejo:\nExample: https://instagram.com/username")
    bot.register_next_step_handler(call.message, lambda m: payment_step(m, call.data))

def payment_step(message, service):
    link = message.text
    bot.send_message(message.chat.id, f"Link: {link}\n\n💰 Payment karo:\nUPI: `{UPI_ID}`\nScreenshot bhejo.", parse_mode='Markdown')
    try:
        bot.send_message(ADMIN_ID, f"NEW ORDER!\nUser: @{message.from_user.username}\nService: {service}\nLink: {link}")
    except: pass

print("Bot Started...")
bot.infinity_polling()
