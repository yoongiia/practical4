n=int(input('Введіть рік:'))
if n % 12 == 0:
    a = 'Рік мавпи'
    print(a)
elif n % 12 == 1:
    a = 'Рік півня'
    print(a)
elif n % 12 == 2:
    a = 'Рік собаки'
    print(a)
elif n % 12 == 3:
    a = 'Рік свині'
    print(a)
elif n % 12 == 4:
    a= 'Рік миші'
    print(a)
elif n % 12 == 5:
    a = 'Рік бика'
    print(a)
elif n % 12 == 6:
    a = 'Рік тигра'
    print(a)
elif n % 12 == 7:
    a = 'Рік кролика'
    print(a)
elif n % 12 == 8:
    a = 'Рік дракона'
    print(a)
elif n % 12 == 9:
    a = 'Рік змії'
    print(a)
elif n % 12 == 10:
    a = 'Рік коня'
    print(a)
elif n % 12 == 11:
    a = 'Рік вівці'
import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Дворяківська Єлизавета')
