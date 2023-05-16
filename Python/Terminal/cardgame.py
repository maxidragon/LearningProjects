import random
cardList = ["9", "9", "9", "9",
            "10", "10", "10", "10",
            "Jack", "Jack", "Jack", "Jack",
            "Queen", "Queen", "Queen", "Queen",
            "King", "King", "King", "King",
            "Ace", "Ace", "Ace", "Ace",
            "Joker", "Joker"]
random.shuffle(cardList)
user1 = []
user2 = []

for i in range(5):
    user1.append(cardList.pop())
    user1.append(cardList[0])
    cardList.pop(0)
    user2.append(cardList[0])
    cardList.pop(0)

cardnumbers = {'9': 9, '10':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14, 'Joker':15}
score1 = 0
score2 = 0
for i in range(0, 5):
    cardU1 = cardnumbers[user1.pop()]
    cardU2 = cardnumbers[user1.pop()]
    if cardU1 > cardU2:
        score1 += 1
    elif cardU1 < cardU2:
        score2 += 1
    elif cardU1 == cardU2:
        print('Tie')
    print(f'{score1}:{score2}')
