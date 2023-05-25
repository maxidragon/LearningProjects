path = r'files/mails.txt'
path2 = r'files/mails1.txt'


with open(path,'r',encoding='utf-8') as file:
    mails = file.read().splitlines()

mails.pop(0)

for mail in mails:
    temp = mail.split(':')[1]
    index = mails.index(mail)
    mails[index] = temp

mail1 = input('Podaj maila: ')
mail2 = input('Podaj maila: ')

if '@' in mail1:
    mails.append(mail1)
if '@' in mail2:
    mails.append(mail2)
with open(path2,'w',encoding='utf-8') as file:
    file.write('emails:\n')
    for mail in mails:
        file.write(f'mailto:{mail}\n')

print(mails)