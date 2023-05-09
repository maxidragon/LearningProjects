'''
names = []
for _ in range(3):
    name = input('Podaj imie: ')
    if (name[-1] != 'a'):
        names.append(name)


print(names)
'''
#1 pokaz liste 2 dodaj 3 usun 4 zakoncz
'''
array = []
while True:
    print('1. Pokaz liste')
    print('2. Dodaj produkt')
    print('3. Usun produkt')
    print('4. Zakoncz program')
    choose = int(input())
    if choose == 1:
        print(array)
    elif choose == 2:
        product = input('Podaj nazwe produktu: ')
        array.append(product)
        print(f'Pomyslnie dodano produkt {product}')
    elif choose == 3:
        product = input('Podaj nazwe produktu: ')
        if product in array:
            array.remove(product)
            print(f'Pomyslnie usunieto produkt {product}')
        else:
            print('Nie ma takiego produktu')

    elif choose == 4:
        break
    else:
        print('Bledny numer!')
print (array)

'''
'''
movies = {"Harry Potter i Kamień Filozoficzny" : 30, "Harry Potter i Komnata Tajemnic" : 35, "Harry Potter i Więzień Azkabanu" : 40}
snacks = {"Popcorn": 10, "Coca-cola" : 5, 'Nachosy' : 5}

for key, value in movies.items():
    print(f'Tytuł: {key} Bilet normalny: {value} Bilet ulgowy {value/2}')
movie = input('Który film wybierasz (podaj nazwe): ')
for key, value in snacks.items():
    print(f'{key} Cena: {value}')
snack = input('Którą przekąske wybierasz (podaj nazwe): ')
print(f'Zaplacisz {movies[movie]+snacks[snack]}')
'''
'''
mylist =[
    number
    for number in range(1, 31)
    if number % 5 == 0 and number % 2 != 0
]
print(mylist)
'''
people = [1, 3, [{
    "IcFDG2bO9AYDF651DoyH": {'name': 'John', 'age': 27, 'sex': 'Male'},
    "KcD9ntE6IRM59vkVta1k": {'name': 'Marie', 'age': 22, 'sex': 'Female'},
    "yDlgcn99xPc19mYXcRmy": {'name': 'Pawel', 'age': 25, 'sex': 'Female'},
    "cpQh6GiAbBdGv35NDoTk": {'name': 'Nabeel', 'age': 17, 'sex': 'Male'},
    "12BifzWxCQySKgLhgahC": {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
    "QLnmg0pzlLj9x7c7DlLv": {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
    "To47urX0DUznWmOxGZ6H": {'name': 'Lori', 'age': 27, 'sex': 'Male'},
    "KQ4bir3y4tlkbG69I7zq": {'name': 'Marie', 'age': 42, 'sex': 'Female'},
    "94cp4hsyZP2BnCh4D34z": {'name': 'Piotr', 'age': 25, 'sex': 'Female'},
    "Vr4wRdkljeEs46Czxo54": {'name': 'Chiara', 'age': 17, 'sex': 'Male'},
}]]

#print(people[2][0]['Vr4wRdkljeEs46Czxo54']['age'])

identificators = {'identificators': [
    {'id': 'IcFDG2bO9AYDF651DoyH', 'name': 'Pawel', 'age': 27, 'sex': 'Male'},
    {'id': 'KcD9ntE6IRM59vkVta1k', 'name': 'Marie', 'age': 22, 'sex': 'Female'},
    {'id': 'yDlgcn99xPc19mYXcRmy', 'name': 'Piotr', 'age': 25, 'sex': 'Female'}
]}


marks = {"marks": [
    "Piotr", (2, 1, 2, 3, 2, 3),
    "Pawel", (4, 2, 1, 3, 4)
]}
ratings = [
    {'name': "Piotr", 'ratings': (2, 1, 2, 3, 2, 3), 'behaviour': 4},
    {'name': "Pawel", 'ratings': (4, 2, 1, 3, 4), 'behaviour': 2}
]
#print(marks['marks'][3][-1])

years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]

ages = [
    2022-age
    for age in years_of_birth


]
print(ages)