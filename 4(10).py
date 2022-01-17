a=str(input('Введення зросту та маси в дюймах та фунтах?(так, ні):'))
if a=='так':
    mas=float(input('Введіть масу:'))
    zr=float(input('Введіть зріст:'))
    im=(mas/(zr**2))*703
elif a=='ні':
    mas=float(input('Введіть масу в кілограмах:'))
    zr=float(input('Введіть зріст в метрах:'))
    im=mas/(zr**2)
print('Ваш індек маси тіла:',im)
import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Дворяківська Єлизавета')
