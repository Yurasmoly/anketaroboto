from flask import Flask, request, redirect
import csv
import os
from datetime import datetime

app = Flask(__name__)

# Налаштування: ім'я файлу, куди зберігати дані
CSV_FILE = 'vidguky.csv'

# Перевіряємо, чи існує файл. Якщо ні - створюємо заголовки
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Дата/Час', 'Оцінка', '3 слова', 'Що сподобалось', 'Що не так', 'Побажання'])

@app.route('/')
def index():
    # Ця функція просто читає ваш HTML файл і показує його в браузері
    with open('index.html', 'r', encoding='utf-8') as file:
        return file.read()

@app.route('/submit', methods=['POST'])
def submit():
    # Отримуємо дані з форми
    rating = request.form.get('Оцінка')
    words = request.form.get('3_слова_про_курс')
    liked = request.form.get('Що_сподобалось')
    disliked = request.form.get('Що_не_сподобалось')
    wishes = request.form.get('Побажання')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Записуємо у файл
    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([timestamp, rating, words, liked, disliked, wishes])

    # Повертаємо просту сторінку подяки
    return """
    <h1>Дякуємо! Ваша відповідь збережена на комп'ютері ✅</h1>
    <a href='/'>Повернутися назад</a>
    """

if __name__ == '__main__':
    # Запускаємо сервер на порту 5000
    print("🚀 Сервер запущено! Відкрийте в браузері: http://127.0.0.1:5000")
    app.run(debug=True, port=5000)