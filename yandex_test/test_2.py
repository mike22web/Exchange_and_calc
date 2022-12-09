# Поиск и сортировка данных согласно условиям.
# Внесение результатов поиска в отдельную таблицу

import sqlite3

conn = sqlite3.connect('business.db')
cursor = conn.cursor()
cursor1 = conn.cursor()
cursor2 = conn.cursor()
cursor3 = conn.cursor()

# Постройте таблицу, где для каждой страны посчитано число компаний, удволетворяющих условиям:
# 1) штаб квартира компании находится в этой стране
# 2) число сотрудников компании не менее 1000 человек

cursor1.execute('''SELECT id, country_id FROM Cities''')
city = cursor1.fetchall()
cursor2.execute('''SELECT id, name FROM Countries''')
country = cursor2.fetchall()
cursor3.execute('''SELECT city_id, labors FROM Companies''')
company = cursor3.fetchall()
dict_result = {i[0]: [i[1], 0] for i in country}
for i in company:
    if i[1] >= 1000:
        for j in city:
            if i[0] == j[0]:
                for key, value in dict_result.items():
                    if key == j[1]:
                        dict_result[key][1] += 1
print(dict_result)
for value in dict_result.values():
    cursor.execute('''INSERT INTO Result(name_company, quantity) VALUES(?, ?)''',
                   (value[0], value[1]))
conn.commit()
cursor.execute('''SELECT * FROM Result''')
result = cursor.fetchall()
print(result)
print(f'city {city}')
print(f'country {country}')
print(f'company {company}')
