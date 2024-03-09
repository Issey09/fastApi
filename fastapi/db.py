import sqlite3

# Подключение к базе данных SQLite
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Выполнение SQL-запроса для извлечения данных
cursor.execute('SELECT * FROM table_name')  # Замените 'table_name' на имя вашей таблицы

# Получение результатов запроса
rows = cursor.fetchall()

# Вывод результатов на экран


# Закрытие соединения с базой данных
conn.close()