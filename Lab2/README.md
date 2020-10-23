# 1-5

### Встановлення pipenv
```
sudo apt-get install pipenv
```
### Створення віртуального середовища для python3
```
pipenv --three
```
### Запуск віртуального середовища і встановлення необхідних бібліотек
``` 
pipenv install requests
pipenv install ntplib
```

### Результат роботи app.py
```
========================================
Результат без параметрів: 
No URL passed to function
========================================
Результат з правильною URL: 
Time is:  08:35:35 PM
Date is:  10-22-2020
```

# 6
###  Pytest пакет варто відокремити він не є необхідним для роботи програми лише для тестування розробником
``` 
pipenv install pytest --dev
```
# 7 
### Успішно пройдені тести
```
======================================== test session starts ========================================
platform linux -- Python 3.7.3, pytest-6.1.1, py-1.9.0, pluggy-0.13.1
rootdir: /home/user/ISPT/ISTP/Lab2
collected 4 items                                                                                   

tests/tests.py ....                                                                           [100%]

========================================= 4 passed in 0.80s =========================================
```
# 10
### Команда виконувалася в середовищі pipenv, з директорії tests/ 
### resault.txt -> test/resault.txt 
```
python3 -m pytest tests.py >resault.txt ; python3 ../app.py >> resault.txt
``` 
