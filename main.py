from flask import Flask, request, jsonify
import telegram
import json

# ✅ Вписали токен и ID чата напрямую
TOKEN = "7694671048:AAGKtL9DRneqCv-2nk48eNwAkZSYKHNitBU"
CHAT_ID = "864066537"

bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

booked_dates = []

@app.route('/')
def home():
    return "Telegram Bot is running!"

@app.route('/book', methods=['POST'])
def book_date():
    global booked_dates
    data = request.json
    date = data.get("date")
    name = data.get("name")

    if not date or not name:
        return jsonify({"status": "error", "message": "Дата и имя обязательны!"}), 400

    if date in booked_dates:
        return jsonify({"status": "error", "message": "Дата уже занята"}), 400

    booked_dates.append(date)

    # ✅ Исправлено! Теперь бот отправляет сообщение в Telegram
    message = f"📅 Новая бронь:\nДата: {date}\nИмя: {name}"
    bot.send_message(chat_id=CHAT_ID, text=message)

    return jsonify({"status": "success"})

@app.route('/get_booked_dates', methods=['GET'])
def get_booked_dates():
    return jsonify(booked_dates)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)