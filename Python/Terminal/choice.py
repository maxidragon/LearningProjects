import random
'''
Napisz krótką grę w której masz 3 ruchy 
Za każdym razem masz szansę spotkać po drodzę SKARB lub NIC.
Skrzynki mają różne kolory.
Kolor skarbu oznacza jak rzadka jest ta skrzynka
szara - 60%
niebieska - 25%
fioletowa - 10%
platynowa - 5%
Ustaw, że jest 30% szansy, że nie spotkasz niczego. 70%, że będzie skarb.
Ustaw złoto jako to co może "wypaść" ze skarbu:
szara - 1000,
niebieska - 3000,
fioletowy - 6000,
platynowa - 10000
'''
decision = [True, False]
decision_probability = [0.7, 0.3]
chests = {'Szara':1000, 'Niebieska':3000, 'Fioletowa':6000, 'Platynowa':10000}
chests_probability = [0.6, 0.25, 0.1, 0.05]
money = 0
for _ in range(3):
    is_chest = random.choices(decision, decision_probability)[0]
    if is_chest:
        chest = random.choices(list(chests.keys()), chests_probability)[0]
        money += chests[chest]
        print(f'W tej rundzie zdobyłeś: {chests[chest]}')
    else:
        print('Wylosowałes nic')

    play = int(input('Czy chcesz grać dalej? 1 - tak: '))
    if play != 1:
        break

print(f'Money: {money}')
#false 0, [], '',

