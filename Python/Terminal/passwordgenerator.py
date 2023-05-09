# Haslo musi zawierac:
# -male litery
# -wielkie litery
# Hasło może zawierać:
# -znaki specjalne
# -numery
# Dlugosc hasła wybiera uzytkownik
from random import choice
import string

numbers = string.digits
smallletters = string.ascii_lowercase
bigletters = smallletters.upper()
specials = string.punctuation

pool = smallletters + bigletters
isNumbers = input('Czy chcesz numery? 1-Tak 2-Nie ')
pool += numbers if isNumbers=='1' else ''
isSpecials = input('Czy chcesz znaki specjalne? 1-Tak 2-Nie ')
pool += specials if isSpecials=='1' else ''
length = ''
while True:
    try:
        length = int(input('Podaj dlugosc hasla <8, 24>: '))
    except ValueError as e:
        print(f'Error: {e}')
    else:
        if length >= 8 and length <= 24:
            break

result = ''
for i in range(0, length):
    result += choice(pool)

print(result)