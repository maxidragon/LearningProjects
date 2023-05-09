path = r'/Users/peplaj/Desktop/korepetycje/maks/teksty/przyklad.txt'

#r - read (domyślny)
#w - write (zapis)
#a - append (dopisywanie)

# file = open(path,'a')
# file.write('dzisiaj jest ładna pogoda')
# file.close()

#wywolanie context managera
#rozne dowolne operacje
#wywoalnie contect managera

with open(path,'r',encoding='utf-8') as file:
    content = file.read().splitlines()

print(content)
for player in content:
    print(player)