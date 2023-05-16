

#r - read
#w - write
#a - append

# file = open(path,'a')
# file.write('dzisiaj jest ładna pogoda')
# file.close()

with open(path,'r',encoding='utf-8') as file:
    content = file.read().splitlines()

print(content)
for player in content:
    print(player)