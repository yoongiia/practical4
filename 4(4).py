a=200
b=50
c=45.00
d=int(input('Введіть кількість використаних хвилин:'))
e=int(input('Введіть кількість використаних SMS:'))
f=d-a
g=e-b
if f<=0 and g<=0:
    c1=(c*0.05)+c+1.44
    print('Ціна тарифу -',c, 'гривень')
    print('Загальний рахунок -',c1, 'гривень')
elif f>0 and g<=0:
    v=f*0.27
    c1=(c*0.05)+c+1.44+v
    print('Ціна тарифу -',c, 'гривень')
    print('Загальний рахунок -',c1, 'гривень')
elif f<=0 and g>0:
    l=g*0.5
    c1=(c*0.05)+c+1.44+l
    print('Ціна тарифу -',c, 'гривень')
    print('Загальний рахунок -',c1, 'гривень')
else:
    v=f*0.27
    l=g*0.5
    c1=(c*0.05)+c+1.44
    c2=c1+v+l
    print('Ціна тарифу -',c, 'гривень')
    print('Загальний рахунок -',c2, 'гривень')
import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Дворяківська Єлизавета')
