Для запуска необходима уситановка библиотек PyQt5 и Pandas
Главное меню (all_in_one.py) – его запускаем сразу, откуда посредством нажатия на кнопки открываем либо калькулятор , либо конвертер валют
Конвертер валют:

1. Актуальный курс берется с сайта myfin.by с помощью библиотеки pandas и метода read_html(), который возвращает информацию с запрашиваемой страницы в виде списка таблиц.

2. “Enter the amount” - вводим с клавиатуры сумму к обмену, тыкаем Enter

3. “Base” – в выпадающем меню выбираем базовую валюту, относительно которой будет производиться расчет.

Остальные ячейки заполняются автоматически после выбора (или изменения) базовой валюты

4. При изменении суммы обмена (и нажатия Enter) – значения в ячейках напротив валют также меняются автоматически

5. Кнопка “Main menu” возвращает в главное меню))

Main menu (all_in_one.py ) – we launch it immediately, from where by clicking on the buttons we open either a calculator or a currency converter
Currency Converter:
To run, you need to install the PyQt5 and Pandas libraries

1. The current course is taken from the website myfin.by using the pandas library and the read_html() method, which returns information from the requested page in the form of a list of tables.

2. “Enter the amount” - enter the amount to be exchanged from the keyboard, press Enter

3. “Base" – in the drop-down menu, select the base currency against which the calculation will be made.

The remaining cells are filled in automatically after selecting (or changing) the base currency

4. When changing the exchange amount (and pressing Enter) – the values in the cells opposite the currencies also change automatically

5. The “Main menu” button returns to the main menu)
