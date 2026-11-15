import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm alive. My creator is Rapheal Arigho.")

async def creator(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("My creator is Rapheal Arigho.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "who created you" in text or "who made you" in text or "who is your creator" in text:
        await update.message.reply_text("My creator is Rapheal Arigho.")
    else:
        await update.message.reply_text(f"You said: {update.message.text}")

def main():
    token = os.environ.get("BOT_TOKEN")
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("creator", creator))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
