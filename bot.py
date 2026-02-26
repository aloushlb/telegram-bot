from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, ContextTypes

TOKEN = "8772465610:AAFS70a0fqgwf780u9LSW-GpUoHfDjv7VO0" # 
ADMIN_CHAT_ID = 854268073  # رقمك

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
