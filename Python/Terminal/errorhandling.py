from random import choice
import string

numbers = string.digits
smallLetters = string.ascii_lowercase
bigLetters = smallLetters.upper()
specials = string.punctuation

pool = smallLetters + bigLetters
isNumbers = input('Numbers? 1-Yes 2-No ')
pool += numbers if isNumbers=='1' else ''
isSpecials = input('Special characters? 1-Yes 2-No ')
pool += specials if isSpecials=='1' else ''

try:
    length = int(input('Password length: '))
except ValueError as e:
    print(f'Error occured: {e}')
    length = 14

result = ''
for i in range(0, length):
    result += choice(pool)

print(result)

