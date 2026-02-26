from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_CHAT_ID = int(os.getenv("ADMIN_CHAT_ID"))

# عند ضغط زر
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user = query.from_user.first_name
    choice = query.data

    await context.bot.send_message(
        chat_id=ADMIN_CHAT_ID,
        text=f"Answer is: {choice}"
    )
    
    # يمكن تعديل رسالة الصورة لتظهر الاختيار
    await query.edit_message_caption(caption=f"اخترت: {choice}")

# عند استقبال صورة
async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("A", callback_data="A"), InlineKeyboardButton("B", callback_data="B")],
        [InlineKeyboardButton("C", callback_data="C"), InlineKeyboardButton("D", callback_data="D")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    photo_file = update.message.photo[-1]
    # نرسل الصورة مع الأزرار
    await update.message.reply_photo(
        photo=photo_file.file_id,
        caption="اختر أحد الخيارات:",
        reply_markup=reply_markup
    )

app = ApplicationBuilder().token(TOKEN).build()

# نضيف handlers
app.add_handler(CallbackQueryHandler(button_click))
app.add_handler(MessageHandler(filters.PHOTO, photo_handler))

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
