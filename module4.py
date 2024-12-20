
print("-"*45)
print('        Модуль 4 - КМ-42 Ільчук Іван')
print('             1 - запуск програми')
print('            0 - вихід із програми')
print("-"*45)
action = "" #створює порожню змінну яка буде потім заповнена обраною дією
while True:
    action = input() #приймає дію 
    try: #пробує перетворити строку на ціле число
        action = int(action)
    except: #якщо не вийшло
        pass #нічого не робить
    else: #якщо вийшло
        if action == 1:
            break #продовжує виконання програми
        elif action == 0:
            quit() #закриває програму

while True: #запитує номер завдання допоки не вибереться існуюче
    task = input("Оберіть завдання для запуску: ") #записує обране завдання у змінну
    try:
        task = int(task) #пробує перетворити введений рядок на ціле число
    except: #якщо не введено ціле число
        print("Помилка при введенні номеру завдання")
    else: #якщо введено ціле число
        if task in [1,2]: #перевірка на існування завдання
            break #виходить із циклу
        else: #якщо завдання не існує
            print("Завдання", str(task),"не існує") 

match task: #запускає потрібну програму в залежності від обраного завдання
    case 1: #завдання 1

        import sys
        point_coords = [[None,None],[None,None],[None,None]] #створює список з двома іншими списками, куди згодом
                                                             #будуть додані координати точок
        def get_points(x,y,radius): #опис функції, яка повертає кількість очок за попадання в точку (x,y)
            points = 10
            circle_num = 1 #номер кола
            distance_squared = x**2 + y**2 #квадрат відстані точки (x,y) від центру мішені
            while distance_squared - (radius * circle_num) ** 2 > sys.float_info.epsilon and points > 0: #віднімає 1 очко за кожне коло, в яке
                points -= 1                                                                     #точка (x,y) не влучила
                circle_num += 1
            return points 

        def get_total_points(x1,y1,x2,y2,x3,y3,radius): #підраховує очки за 3 точки
            return get_points(x1,y1,radius) + get_points(x2,y2,radius) + get_points(x3,y3,radius)
        
        print("-"*82)
        print('  Умова: Мішень для стрільби являє собою концентричні кільця з центром на початку')
        print('    координат. радіус внутрішнього кільця {(десятки)} - 1см. Ширина всіх інших')
        print('   кілець - по 1см. Написати функцію, яка за координатами трьох точок попадання') 
        print('    (х1, у1), (х2, у2) і (х3, у3) обчислює суму вибитих очок. Координати уводити.')
        print('                       Натисніть enter для запуску завдання')
        print("-"*82)
        input()

        print("Формат введення координат: \"<x>,<y>\"")
        print("1 одиниця координат = 1 сантиметр")


        for i in range(3): #повторює тіло циклу для трьох точок
            while True:
                try:
                    point_coords[i] = input("Координати точки " + str(i+1) + ": ").split(",") #додає пару координат до списку
                    if len(point_coords[i]) != 2: 
                        raise Exception("point must have 2 coordinates") #видає помику якщо в парі не 2 значення
                    for j in range(2):
                        point_coords[i][j] = float(point_coords[i][j]) #перетворює значення в парі на float
                except:
                    print("Помилка: неправильні вхідні дані")
                else:
                    break #виходить із циклу while якщо немає помилок

        print("Ви набрали", \
        get_total_points(point_coords[0][0],point_coords[0][1],point_coords[1][0],point_coords[1][1],point_coords[2][0],point_coords[2][1],1), \
        "очок")
        #пише результат
    case 2: #завдання 2
        print("-"*45)
        print('          Функція - Insert(s,s1,n).')
        print(' Призначення - вставка в рядок s підрядка s1,')
        print('           починаючи з позиції n.')
        print('     Натисніть enter для запуску завдання')
        print("-"*45)
        input()
        #початок коду завдання 2
        def Insert(s,s1,n):
            out_string = s[:n] #додає до рядку 
            out_string = out_string + s1
            out_string = out_string + s[n:]
            return out_string # вставляє substring в in_string на позиції n
        string = input("Введіть рядок: ")
        substring = input("Введіть підрядок: ")
        index = int(input("Ввеіть позицію, на якій вставити підрядок: "))
        print("\nРезультуючий рядок:",Insert(string,substring,index))
       
    #кінець match оператору


print("\nКінець програми")
