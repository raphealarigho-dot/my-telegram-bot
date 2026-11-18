import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

app_web = Flask(__name__)

@app_web.route('/')
def home():
    return "Mirage Bot is running!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am Mirage. Ask me anything.")

async def creator(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("My creator is Rapheal.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "who created you" in text or "who made you" in text or "who is your creator" in text:
        await update.message.reply_text("My creator is Rapheal.")
    else:
        await update.message.reply_text(f"You said: {update.message.text}")

def run_bot():
    token = os.environ.get("BOT_TOKEN")
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("creator", creator))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get("PORT", 10000))
    app_web.run(host="0.0.0.0", port=port)
