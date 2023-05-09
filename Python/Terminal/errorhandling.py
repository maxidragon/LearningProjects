from random import choice
import string

numbers = string.digits
smallLetters = string.ascii_lowercase
bigLetters = smallLetters.upper()
specials = string.punctuation

pool = smallLetters + bigLetters
isNumbers = input('Czy chcesz numery? 1-Tak 2-Nie ')
pool += numbers if isNumbers=='1' else ''
isSpecials = input('Czy chcesz znaki specjalne? 1-Tak 2-Nie ')
pool += specials if isSpecials=='1' else ''

try:
    length = int(input('Podaj dlugosc hasla: '))
except ValueError as e:
    print(f'Error occured: {e}')
    length = 14

print('to sie zawsze wykona')
result = ''
for i in range(0, length):
    result += choice(pool)

print(result)

#wymagane
#try(linijka/i ktora/e powoduja blad/bledy)
#except(co ma sie wydarzyc gdy wystapi blad)

#opcjonalne
#else(KONTYNUACJA BLOKU TRY(linijki zalezne od TRY)co ma sie wydarzyc gdy do bledu nie dojdzie)
#finally(to co w tym bloku zawsze sie wykona)