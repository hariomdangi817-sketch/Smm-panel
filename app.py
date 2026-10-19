# app.py - FREE SMM PANEL BOT
# Install: pip install python-telegram-bot

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = "8959233284:AAFhxYO5dJysBNhgub2sZ3IaJQ9pFEq5y1Y"
ADMIN_ID = 8907869447  # Yahan apni Telegram ID dalo @userinfobot se lelo
UPI_ID = "rajulaldangi532@ybl"

# Tumhare Services + Tumhara Profit
SERVICES = {
    "insta_followers": {"name": "📸 Instagram Followers 1K", "price": 70, "cost": 30},
    "insta_likes": {"name": "❤️ Instagram Likes 1K", "price": 40, "cost": 15},
    "yt_views": {"name": "▶️ YouTube Views 1K", "price": 50, "cost": 20},
    "tg_members": {"name": "✈️ Telegram Members 1K", "price": 100, "cost": 40},
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = []
    for key, s in SERVICES.items():
        keyboard.append([InlineKeyboardButton(f"{s['name']} - ₹{s['price']}", callback_data=key)])
    
    await update.message.reply_text(
        "🔥 *SMM PANEL FOR SALE* 🔥\n\nSabse Sasta SMM Panel - Instant Delivery\n\nService select karo:",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode='Markdown'
    )

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    service = SERVICES[query.data]
    context.user_data['selected'] = query.data
    
    await query.message.reply_text(
        f"✅ {service['name']}\n\nPrice: ₹{service['price']}/1K\n\nApna Link/Username bhejo\nExample: https://instagram.com/username"
    )

async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if 'selected' not in context.user_data:
        return
    service = SERVICES[context.user_data['selected']]
    link = update.message.text
    context.user_data['link'] = link
    
    await update.message.reply_text(
        f"Link: {link}\nService: {service['name']}\n\n💰 *Payment karo:*\nUPI: `{UPI_ID}`\nAmount: ₹{service['price']}\n\nPayment ke baad screenshot bhejo.",
        parse_mode='Markdown'
    )
    # Admin ko bhejo
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"NEW ORDER!\nUser: @{update.effective_user.username}\nService: {service['name']}\nLink: {link}\nProfit: ₹{service['price']-service['cost']}"
    )

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_click))
app.add_handler(app.builder()._handlers) # simplified

# Message handler for link
from telegram.ext import MessageHandler, filters
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))

print("Bot Started...")
app.run_polling()
