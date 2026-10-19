import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8959233284:AAFhxYO5dJysBNhgub2sZ3IaJQ9pFEq5y1Y"
ADMIN_ID = 8907869447 
UPI_ID = "rajulaldangi532@ybl"

SERVICES = {
    "insta_followers": {"name": "📸 Instagram Followers 1K", "price": 70},
    "insta_likes": {"name": "❤️ Instagram Likes 1K", "price": 40},
    "yt_views": {"name": "▶️ YouTube Views 1K", "price": 50},
    "tg_members": {"name": "✈️ Telegram Members 1K", "price": 100},
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(f"{s['name']} - ₹{s['price']}", callback_data=key)] for key, s in SERVICES.items()]
    await update.message.reply_text("🔥 *SMM PANEL* 🔥\nService select karo:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    context.user_data['selected'] = query.data
    service = SERVICES[query.data]
    await query.message.reply_text(f"✅ {service['name']}\nPrice: ₹{service['price']}\n\nApna Link bhejo:")

async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if 'selected' not in context.user_data:
        return
    service = SERVICES[context.user_data['selected']]
    link = update.message.text
    await update.message.reply_text(f"Link: {link}\n💰 Payment: UPI `{UPI_ID}` - ₹{service['price']}\nScreenshot bhejo.", parse_mode='Markdown')
    try:
        await context.bot.send_message(chat_id=ADMIN_ID, text=f"NEW ORDER\nUser: @{update.effective_user.username}\nService: {service['name']}\nLink: {link}")
    except: pass

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))
    print("Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()
