>>> from flask import Flask, request, jsonify
... import telegram
... import json
... import os
... 
... TOKEN = os.getenv("7694671048:AAGKtL9DRneqCv-2nk48eNwAkZSYKHNitBU")  # Токен бота
... CHAT_ID = os.getenv("864066537")  # ID чата
... bot = telegram.Bot(token=TOKEN)
... 
... app = Flask(__name__)
... 
... # Храним брони в памяти (лучше позже заменить на базу данных)
... booked_dates = []
... 
... @app.route('/')
... def home():
...     return "Telegram Bot is running!"
... 
... @app.route('/book', methods=['POST'])
... def book_date():
...     global booked_dates
...     data = request.json
...     date = data.get("date")
... 
...     if date in booked_dates:
...         return jsonify({"status": "error", "message": "Дата уже занята"}), 400
... 
...     booked_dates.append(date)
...     bot.send_message(CHAT_ID, f"📅 Новая бронь: {date}\nИмя: {data['name']}")
... 
...     return jsonify({"status": "success"})
... 
... @app.route('/get_booked_dates', methods=['GET'])
... def get_booked_dates():
...     return jsonify(booked_dates)
... 
... if __name__ == '__main__':
