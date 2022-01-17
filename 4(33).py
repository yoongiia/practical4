y = int(input('Введіть рік:'))
if y % 4 == 0 and y % 100 != 0:
    print("Високосний")
elif y % 400 == 0:
    print("Високосний")
else:
    print("Не високосний")
import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Дворяківська Єлизавета')
