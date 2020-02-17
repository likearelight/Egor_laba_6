#За s-назвою місяця визначити відповідну пору року.
#Петухов Єгор Б19_д/122Б
from enum import Enum
while True:
    while True:
            try:
                s = int(input('month: '))
                break
            except:
                print('Тільки числа')
    while s < 0 or s > 13:
        s = int(input('Введіть введіть вірний номер місяця, введіть заново :' ))

    class month(Enum):
        January = 1
        February = 2
        March = 3
        April = 4
        May = 5
        June = 6
        July = 7
        August = 8
        September = 9
        October = 10
        November = 11
        December = 12



    class season(Enum):
        Winter = 1
        Spring = 2
        Summer = 3
        Autumn = 4

    if s == month.January.value or s == month.February.value or s == month.December.value:
        print(season.Winter.name)
    elif s == month.March.value or s == month.April.value or s == month.May.value:
        print(season.Spring.name)
    elif s == month.June.value or s == month.July.value or s == month.August.value:
        print(season.Summer.name)
    elif s == month.September.value or s == month.October.value or s == month.November.value:
        print(season.Autumn.name)
    result = input('Хочете ще раз ввести час? якщо так натисніть 1, а якщо будь яку іншу кнопку: ')
    if result == '1':
        continue
    else:
        break