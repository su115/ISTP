# 2
### Завдання виконано в examples.py Відповіді в коментарях.
### Приклад виводу example.py
```
 --------------------
          I
True False None

 --------------------
          II
12
1234567900
4

 --------------------
          III
##########
#        #
#        #
#        #
#        #
#        #
#        #
#        #
#        #
##########

 --------------------
          IV
Виключення!
4 елементу у списку немає.

 --------------------
          V
#! /bin/python3

 --------------------
          VI
sum: 1 + 4 = 5 
sum: first + secound = firstsecound

 --------------------
```
# 3
## I
```
We are in the __main__
2020-10-22 06:50:25.235200
linux
```
## II
### Програма виводить  поточний час і платформу ОС, а також якщо з параметром  -о то також вивуде видозмінене повідомлення
### a) python3 . -h виведе help даної програми це можливо завдяки
###
### b) python3 . -o "Some text"
```
З консолі було передано аргумент
========== >> Some text << ==========
```
### d) python3 . --logs 
```
2020-10-22 07:36:52,251 root INFO: Тут буде просто інформативне повідомлення
2020-10-22 07:36:52,251 root WARNING: Це Warning повідомлення
2020-10-22 07:36:52,251 root ERROR: Це повідомлення про помилку
```
#
#
## III
### функція в modules/commmon.py
```
def myfoo1(value):
    if value%2==1:value=False
    else:value=True
    for i in range(100):
        if value and i%2 == 0:
            print(i,end=' ')
        elif not value and i%2 == 1:
            print(i,end=' ')
```
#
## IV
### логи записуються в файл mylog.log його вміст після 3 запуску
```
2020-10-22 08:33:16,137 root ERROR: value==0 error
2020-10-22 08:33:32,504 root INFO: you dont get error
2020-10-22 08:33:37,678 root ERROR: value==0 error
```
#
### функція яка веде лог із файла modules/common.py
```
def myfoo2(log,value):

    if value==0:
        log.error('value==0 error')
    else:
        log.info('you dont get error')

```
### щоб код працював треба змінити __main__.py
#
```
logging.basicConfig(level=logging.INFO, format=FORMAT, filename='mylog.log')
```
#### тут додано параметр filename, який записує в файл логи
#

```
# i add this string
parser.add_argument('-p', dest='value',action="store",type=int, help='Моя функція', default=0)
```
#### тут додано ще один параметр до функціоналу програми "-p" який впливатиме на функції я треба було дописати
#
```
    #III
    common.myfoo1(args.value)
    
    #IV
    common.myfoo2(logger,args.value)
``` 
#### виклик самих функцій в функції main
# 
