# 1-3 
#### Ознайомився з docker-compose, Makefile, бііліотекою Flask.
# 4-5 
#### Створив відповідні директорії і копіював відповідні файли в них. Ознайомився з вмістом.
# 6
#### Ініціалізував середовище. Також для тестів. Сайт був не працездатним з трьох причин 
#### 1)Не було локального редіс сервера.Рішення: потрібно було інсталювати redis  на локальний комп'ютер 
#### 2)Застосунок посилався на інший hostname Рішення: замінити в ./my_app/app.py hostname='redis' нa 'localhost' або додати відповідні записи в /etc/hosts хоста. 
#### 3)Застосунок потребував повних шляхів до файлу logs/app.log Рішення: дописати функцію яка створює повний шлях або викликає виключення з відповідеим повідомленням повідомлення. (код варто оптимізувати)
#### Тести пройшли успішно. Помилки не з'явилися однак треба було замінити localhost:5000 на 0.0.0.0:5000
![test success](./images/lab5res.png)
# 7
