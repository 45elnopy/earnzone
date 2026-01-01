
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import requests

TOKEN = "8404928684:AAHIO2ZXYBkr5IttEXZnh_Yooaq4QLx24pk"
API_URL = "http://127.0.0.1:5000/api/message"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    requests.post(f"{API_URL}/register", json={
        "user_id": user.id,
        "username": user.username
    })

    keyboard = [
        [InlineKeyboardButton("🎥 مشاهدة فيديو", web_app={"url": "https://YOUR_WEBAPP_URL"})],
        [InlineKeyboardButton("🎡 عجلة الحظ", web_app={"url": "https://YOUR_WEBAPP_URL/spin.html"})],
        [InlineKeyboardButton("💰 رصيدي", callback_data="balance")]
    ]

    await update.message.reply_text(
        "🎯 مرحبًا بك في EarnZone\nابدأ الربح الآن:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    r = requests.get(f"{API_URL}/balance/{user_id}")
    points = r.json().get("points", 0)
    await query.message.reply_text(f"💰 نقاطك الحالية: {points}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(balance, pattern="balance"))
app.run_polling()
