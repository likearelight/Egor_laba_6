# За датою d, m, y визначити дату наступного і попереднього дня. В програмі врахувати
# наявність високосних років.
#Петухов Єгор Б19_д/122Б
days = range(1, 32)
mounths = range(1, 13)
years = range(1901, 2021)
popered = 0
while True:
    while True:
        try:
            d, m, y = int(input('День: ')), int(input('Місяць: ')), int(input('Роки: '))
            break
        except ValueError:
            print('Введіть правильне значення ')
    if d in days and m in mounths and y in years:
        if y % 4 == 0:
            while m < 1 or m > 12:
                m = int(input("input m!:"))
            if m == 2:
                index = 1
            elif m == 4 or m == 6 or m == 9 or m == 11:
                index = 2
            elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                index = 3

            while d < 1 or (d > 29 and index == 1) or (d > 30 and index == 2) or (d > 31 and index == 3):
                d = int(input("Кількість днів неправильна введіть заново:"))

            if (d == 29 and index == 1) or (d == 30 and index == 2) or (d == 31 and index == 3):
                sled = 1
            else:
                sled = d + 1
            if (d == 1 and index == 1) or (d == 1 and index == 2):
                popered = 31
            elif (m == 3 and d == 1):
                popered = 29
            elif (m == 5 and d == 1) or (m == 7 and d == 1) or (m == 10 and d == 1) or (m == 12 and d == 1):
                popered == 30
            elif m == 1:
                popered = 31
            else:
                popered = d - 1

            print('наступний день-', sled ,"попередній день -", popered)

        else:
            while m < 1 or m > 12:
                m = int(input("input m!:"))
            if m == 2:
                index = 1
            elif m == 4 or m == 6 or m == 9 or m == 11:
                index = 2
            elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
                index = 3

            while d < 1 or (d > 28 and index == 1) or (d > 30 and index == 2) or (d > 31 and index == 3):
                d = int(input("Кількість днів неправильна, введіть заново:"))

            if (d == 28 and index == 1) or (d == 30 and index == 2) or (d == 31 and index == 3):
                sled = 1
            else:
                sled = d + 1
            if (d == 1 and index == 1) or (d == 1 and index == 2):
                popered = 31
            elif (m == 3 and d == 1):
                popered = 28
            elif (m == 5 and d == 1) or (m == 7 and d == 1) or (m == 10 and d == 1) or (m == 12 and d == 1):
                popered == 30
            elif m == 1 :
                popered = 31
            else:
                popered = d - 1

            print('наступний день-', sled ,"попередній день -", popered)
    else:
        print('Введено не вірні значення!Введіть днів від 1 до 31 ,місяці від 1 до 12 та роки від 1902 до 2020')
    result = input('Хочете запустити заново? Якщо так натисніть 1, якщо ні будь яку іншу клавішу : ')
    if result == '1':
        continue
    else:
        break



