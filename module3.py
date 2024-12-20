
def char_change(string,char_from,char_to): #опис функції яка перетворює усі char_from на char_to
    string1 = "" #порожній рядок який буде повертатись
    if len(char_from) > 1 or len(char_to) > 1: #повертає помилку якщо замість символа введено рядок
        raise ValueError("Invalid character")
    char_from = char_from.lower() #переводить введені символи у нижній регістр
    char_to = char_to.lower()
    for i in range(len(string)):
        if string[i] == char_from: #порівнює i-тий символ рядка із char_from
            string1 = string1 + char_to #додає до нового рядка char_to якщо символ співпадає
        elif string[i] == char_from.upper(): #те саме але для верхнього регістру
            string1 = string1 + char_to.upper()
        else:
            string1 = string1 + string[i] #додає до нового рядка той самий символ якщо він не співпадає із char_from
    return string1 #повертає новий рядок

print("--------------------------------")
print(" Модуль 3 - КМ-42 Ільчук Іван")
print("      1 - запуск програми")
print("     0 - вихід із програми")
print("--------------------------------")
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

print("---------------------------------------------")
print("    Умова: Замінити всі символи 'a' на 'd'  ")
print("     у словах, довжина яких менше обраної.  ")
print("     Натисніть enter для запуску завдання   ")
print("---------------------------------------------")
input()

in_string = input("Введіть строку: ")
maxlen = int(input("Максимальна довжина слова, за якої воно зміниться: "))
new_string = "" #перетворений рядок

words = in_string.split() #створює список усіх введених слів
for i in words:
    if len(i) <= maxlen:
        new_string = new_string + char_change(i,"a","d") + " " #додає перетворене слово до new_string якщо 
        #                                                       його довжина менше або дорівнює maxlen
    else:
        new_string = new_string + i + " " #додає те саме слово в іншому випадку
print()
print("Перетворений рядок:",new_string)

print("\nКінець програми")
