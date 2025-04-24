import logging
import re
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "7657360645:AAH-Pv2InSELdnn2w_YPRSvG-ciBX_zdReY"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

app = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я твой бот.')

async def filter_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text.lower()
    if any(word in text for word in ["скинуть", "денег", "деньги", "скину"]) or \
       any(re.search(pattern, text) for pattern in [r"http[s]?://", r"www\.\w+\.\w+", r"t\.me/\w+"]):
        await update.message.delete()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, filter_message))

app.run_polling()
