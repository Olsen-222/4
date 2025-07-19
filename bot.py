from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from keep_alive import keep_alive  # <-- ВАЖНО: импорт наверху

TOKEN = "8025122407:AAEyvUHHnPM20kDLotw1Cf3VRAjCLiFkgUc"

main_menu = [['Конституция РК', 'УК РК'], ['Закон о госслужбе', 'Закон о коррупции']]
constitution_menu = [['Глава 1', 'Глава 2'], ['⬅️ Назад']]

chapter_texts = {
    'Глава 1': 'Глава 1: Основы конституционного строя...',
    'Глава 2': 'Глава 2: Права и свободы человека и гражданина...',
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
    await update.message.reply_text("🔎 Выберите закон:", reply_markup=reply_markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == 'Конституция РК':
        reply_markup = ReplyKeyboardMarkup(constitution_menu, resize_keyboard=True)
        await update.message.reply_text("📘 Выберите главу Конституции:", reply_markup=reply_markup)
    elif text in chapter_texts:
        await update.message.reply_text(chapter_texts[text])
    elif text == '⬅️ Назад':
        reply_markup = ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
        await update.message.reply_text("🔙 Главное меню", reply_markup=reply_markup)
    elif text == 'УК РК':
        await update.message.reply_text("📕 УК РК скоро будет добавлен.")
    elif text == 'Закон о госслужбе':
        await update.message.reply_text("📕 Закон о государственной службе скоро будет добавлен.")
    elif text == 'Закон о коррупции':
        await update.message.reply_text("📕 Закон о противодействии коррупции скоро будет добавлен.")
    else:
        await update.message.reply_text("Пожалуйста, выберите из меню.")

if __name__ == '__main__':
    keep_alive()  # <-- Запускает веб-сервер для Render
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("✅ Бот запущен и работает!")
    app.run_polling()
