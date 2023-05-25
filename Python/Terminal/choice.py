import random

decision = [True, False]
decision_probability = [0.7, 0.3]
chests = {'Gray':1000, 'Blue':3000, 'Purple':6000, 'Platin':10000}
chests_probability = [0.6, 0.25, 0.1, 0.05]
money = 0
for _ in range(3):
    is_chest = random.choices(decision, decision_probability)[0]
    if is_chest:
        chest = random.choices(list(chests.keys()), chests_probability)[0]
        money += chests[chest]
        print(f'{chests[chest]}')
    else:
        print('Nothing')

    play = int(input('Do you want to play again? 1 - yes: '))
    if play != 1:
        break

print(f'Money: {money}')
#false 0, [], '',

