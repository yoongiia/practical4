lt=input('Введіть букву алфавіту: ')
if (lt=='a' or lt=='e' or lt=='i' or lt=='o' or lt=='u' or lt=='я' or lt=='ю' or lt=='є' or lt=='ї'
    or lt=='и' or lt=='у' or lt=='а' or lt=='е'or lt=='а'or lt=='о' or lt=='у' or lt=='ы' or lt=='э'
    or lt=='я' or lt=='ю' or lt=='ё' or lt=='э' or lt=='и' or lt=='е'):
    rp='Ця буква голосна'
elif lt=='y':
    rp='Ця буква інколи – голосна, а інколи – приголосна'
else: rp='Ця буква - приголосна'
print (rp)
import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Дворяківська Єлизавета')
