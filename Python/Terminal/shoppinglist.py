path = r'C:\Users\Max\PycharmProjects\Informatyka\files/shoppinglist.txt'
# Stworz liste zakupow w pythonie
# 1 - zobacz liste
# 2-dodaj produkt
# 3-usun produkt
# 4-zakoncz tworzenie i zapisz liste w pliku txt
#DODAC SPRAWDZANIE CZY PLIK ISTNEJE
import os

if not os.path.isfile(path):
    with open(path, 'w', encoding='utf-8') as file:
        pass

shoppinglist = []

while True:
    try:
        choice = int(input('1. Zobacz liste \n2. Dodaj produkt \n3. Usun produkt \n4. Zakoncz i zapisz liste\n'))
    except ValueError as e:
        print(f'Error occured: {e}')
    else:
        if choice == 1:
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read().splitlines()
                if content:
                    print(content)
                else:
                    print('Lista jest pusta')
        elif choice == 2:
            with open(path, 'a', encoding='utf-8') as file:
                item = input('Podaj nazwe produktu: ')
                file.write(f'{item}\n')
            pass
        elif choice == 3:
            with open(path, 'r', encoding='utf-8') as file:
                item = input('Podaj nazwe produktu: ')
                content = file.read().splitlines()
                try:
                    content.remove(item)
                except ValueError as e:
                    print('Item does not exist!')
            with open(path, 'w', encoding='utf-8') as file:
                for i in content:
                    file.write(f'{i}\n')
        elif choice == 4:
            break
        else:
            print('Bledny numer')
