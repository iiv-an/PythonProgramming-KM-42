
print("-"*45)
print('        Модуль 5 - КМ-42 Ільчук Іван')
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
        print("-"*82)
        print("       Визначити індекси елементів списку, значення яких належать заданому        ")
        print("   діапазону (тобто не менше заданого мінімуму і не більше заданого максимуму).   ")
        print("                                    Необхідно:                                    ")
        print("                     - заповнити список випадковими числами;                      ")
        print("              - запросити для введення мінімум і максимум діапазону;              ")
        print("      - знайти індекси елементів, значення яких входять в діапазон. Додавати      ")
        print("                        знайдені індекси до нового списку;                        ")
        print("         -вивести загальне число знайдених індексів і окремо всі індекси;         ")
        print("    - елементи списку, які знаходяться за певним індексом, видалити зі списку     ")
        print("                            і занести у новий список.                             ")
        print("-"*82)
        input("Натисніть enter для запуску завдання")
        from random import randint

        list = []
        for i in range(randint(10,20)):
            list.append(randint(-100,100)) #генерує список випадкових цілих значень від -100 до 100
        print("Згенеровано список:\n",list)
        while True:
            try:
                diap = input("Введіть діапазон чисел (x1..x2): ").split("..") #приймає діапазон значень (від diap[0] до diap[1])
                if len(diap) != 2:
                    raise ValueError("invalid list length")
                for i in range(2):
                    diap[i] = float(diap[i])
            except Exception:
                print("Помилка при зчитуванні діапозону")
            else:
                break
        if diap[1] < diap[0]:
            temp = diap[0]
            diap[0] = diap[1]
            diap[1] = temp

        index_list = []
        for i in range(len(list)):
            if list[i] >= diap[0] and list[i] <= diap[1]:
                index_list.append(i)
        ch = "ів" #частка коду яка відповідає за закінчення слова індекс
        if len(index_list) == 1:
            ch = ""
        elif len(index_list) <= 4:
            ch = "и"
        print("Знайдено " + str(len(index_list)) + " індекс" + ch + ":") #f-рядки і jdoodle не дружать 
        print(index_list)

        new_list = []

        for i in index_list:
            new_list.append(list[i])
        removed = 0
        for i in index_list:
            list.pop(i-removed)
            removed += 1

        print("Числа поза діапазоном:\n",list)
        print("Числа в діапазоні:\n",new_list)
    case 2: #завдання 2
        print("-"*82)
        print("         Спираючись на визначення базових операцій на множинах, знайти            ")
        print("         A = {1,2,ee,ww,a,d}, B = {2,a,c,tt,4,3}, F = ((A ∩ B) ∪ (A \ B))         ")
        print("-"*82)
        input("Натисніть enter для запуску завдання")
        A = {1,2,"ee","ww","a","d"}
        B = {2,"a","c","tt",4,3}
        F = lambda A,B: (A&B)|(A-B) #функція для обчислення С
        C = F(A,B)
        print("A =",A)
        print("B =",B)
        print("C = (A ∩ B) ∪ (A \ B)")
        print("C = ",C)
       
    #кінець match оператору


print("\nКінець програми")