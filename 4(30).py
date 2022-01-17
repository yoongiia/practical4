a = 0
while True:
    x = "x"
    a = a + 1
    if (a == 1 or a ==10 ):
        x = x * 3
        print('{:^24s}'.format(x))
    elif (a == 2 or a ==9):
        x = x * 9
        print('{:^24s}'.format(x))
    elif (a == 3 or a ==8):
        x = x * 13
        print('{:^24s}'.format(x))
    elif (a == 4 or a ==7):
        x = x * 15
        print('{:^24s}'.format(x))
    elif (a == 5 or a ==6):
        x = x * 17
        print('{:^24s}'.format(x))
    if a == 10:
        break
import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Дворяківська Єлизавета')
