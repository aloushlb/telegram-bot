from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_CHAT_ID = int(os.getenv("ADMIN_CHAT_ID"))

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user = query.from_user.first_name
    choice = query.data

    await context.bot.send_message(
        chat_id=ADMIN_CHAT_ID,
        text=f" answer is: {choice}"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CallbackQueryHandler(button_click))

print("Bot is running...")

PORT = int(os.getenv("PORT", 10000))
WEBHOOK_PATH = f"/{TOKEN}"
WEBHOOK_URL = f"https://telegram-bot-tzwu.onrender.com{WEBHOOK_PATH}"

app.run_webhook(
    listen="0.0.0.0",
    port=PORT,
    webhook_url=WEBHOOK_URL,
    url_path=TOKEN,
)
