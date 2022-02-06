from random import randint
liste_position = []
mine = 0
while mine < 20:
    x=randint(1, 10)
    y=randint(1, 10)
    while [x,y] not in liste_position:
        liste_position.append([x,y])
        mine+=1

print(liste_position)

