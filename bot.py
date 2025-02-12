import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Твій токен бота
TOKEN = '7691652621:AAHn5ZSLt44h8raB6yQBAVJ-E4rK3r9AX7Y'
bot = telebot.TeleBot(TOKEN)

@bot.chat_join_request_handler()
def handle_chat_join_request(request: telebot.types.ChatJoinRequest):
    """Обробка заявок на вступ у канал: надсилаємо текст + фото + кнопку"""
    user_id = request.from_user.id  # ID користувача
    photo_path = "photo.jpg"  # Локальне фото (або заміни на URL)
    
    # Створюємо кнопку з посиланням
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton("Подати заявку", url="https://t.me/+PhGJfAaSF343NmVi")  # Заміни посилання
    keyboard.add(button)

    with open(photo_path, "rb") as photo:
        bot.send_photo(
            chat_id=user_id,
            photo=photo,
            caption="Привіт! Щоб зв’язатися зі мною, натисни кнопку нижче 👇",
            reply_markup=keyboard
        )

# Запуск бота
bot.infinity_polling(allowed_updates=telebot.util.update_types)
