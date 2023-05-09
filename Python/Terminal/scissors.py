
def game(user1, user2):
    if user1 == 0 and user2 == 1:
        return(1)
    elif user1 == 1 and user2 == 2:
        return(1)
    elif user1 == 2 and user2 == 0:
        return(1)
    elif user1 == 1 and user2 == 0:
        return(2)
    elif user1 == 2 and user2 == 1:
        return(2)
    elif user1 == 0 and user2 == 2:
        return(2)
    elif (user1 == 0 and user2 == 0) or (user1 == 1 and user2 == 1) or (user1 == 2 and user2 == 2):
        return(0)
def choice():
    user1 = int(input('User1: '))
    user2 = int(input('User2: '))
    return [user1, user2]

#0 - paper
#1 - stone
#2 - scissors
score_1 = 0
score_2 = 0
while score_1 < 3 and score_2 < 3:
    a,b = choice()
    g = game(a, b)
    if g == 1:
        print('Punkt zdobywa user 1')
        score_1 += 1
    elif g == 2:
        print('Punkt zdobywa user 2')
        score_2 += 1
    elif g == 0:
        print('Remis')
    else:
        print('Bledny wybor!')
    print(f'{score_1}:{score_2}')
