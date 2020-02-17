#Значення змінної х, що позначає деяку суму грошей в валюті р, замінити величиною цієї жсумі в гривнях
#Петухов Єгор Б19_д/122Б
from enum import Enum
while True:
    while True:
        try:
            x = float(input('Введіть суму :'))
            break
        except ValueError:
            print('Тільки числа')

    print('Виберіть бажану валюту USD = 1, EUR = 2, CZK = 3, PLN = 4 ')
    p = int(input('currency:'))
    while p < 0 or p > 4:
        p = int(input('Перевірте чи вірно введяне число!'))
    class converter(Enum):
        USD = 1
        EUR = 2
        CZK = 3
        PLN = 4


    if p == converter.USD.value:
        print(x*25)
    elif p == converter.EUR.value:
        print(x*30)
    elif p == converter.CZK.value:
        print(x*0.9)
    elif p == converter.PLN.value:
        print(x*5.8)
    result = input('Хочете ще раз ввести час? якщо так натисніть 1, а якщо ні будь яку іншу кнопку')
    if result == '1':
        continue
    else:
        break