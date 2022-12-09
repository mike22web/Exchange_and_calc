# Создание БД с таблицами и заполнение их данными

import sqlite3

conn = sqlite3.connect('business.db')
cursor = conn.cursor()
# name - название
# population - численность населения
# founded - год основания
# country_id - id страны
cursor.execute('''CREATE TABLE IF NOT EXISTS Cities(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, population INT,
                founded INT, country_id INT)''')
# Countries - список стран
# id - первичный ключ
# name - название
# population - численность населения
# gdp - валовый продукт в долларах
cursor.execute('''CREATE TABLE IF NOT EXISTS Countries(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, population INT,
                gdp INT)''')
# Companies - компании
# id - первичный ключ
# name - название
# city_id - город в котором находится штаб-квартира
# revenue - годовая выручка в долларах
# labors - численность сотрудников
cursor.execute('''CREATE TABLE IF NOT EXISTS Companies(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, city_id INT,
                revenue INT, labors INT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Result(id INTEGER PRIMARY KEY AUTOINCREMENT, name_company TEXT, 
                quantity INT)''')
lst_city = [('Moscow', 18, 1147, 1), ('Minsk', 2, 1067, 2), ('NewYork', 20, 1624, 3), ('SPB', 6, 1703, 1),
            ('Toronto', 3, 1793, 4)]
lst_country = [('Russia', 150, 10), ('Belarus', 10, 1), ('USA', 200, 10), ('Canada', 100, 8)]
lst_company = [('c1', 1, 100, 2000), ('c2', 3, 100, 5000), ('c3', 2, 50, 2500),
               ('c4', 2, 100, 2500), ('c5', 3, 100, 1100), ('c6', 4, 50, 1500),
               ('c1', 1, 100, 2000), ('c2', 2, 100, 5000), ('c3', 5, 50, 2500)]
for i in lst_city:
    cursor.execute('''INSERT INTO Cities(name, population, founded, country_id) VALUES(?, ?, ?, ?)''',
                   (i[0], i[1], i[2], i[3]))
for i in lst_country:
    cursor.execute('''INSERT INTO Countries(name, population, gdp) VALUES(?, ?, ?)''',
                                       (i[0], i[1], i[2]))
for i in lst_company:
    cursor.execute('''INSERT INTO Companies(name, city_id, revenue, labors) VALUES(?, ?, ?, ?)''',
                   (i[0], i[1], i[2], i[3]))
conn.commit()
