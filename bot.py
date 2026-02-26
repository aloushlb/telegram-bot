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

    # رسالة لك
    await context.bot.send_message(
        chat_id=ADMIN_CHAT_ID,
        text=f" Hi {user} , answer is: {choice}"
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CallbackQueryHandler(button_click))

print("Bot is running...")
app.run_polling()
