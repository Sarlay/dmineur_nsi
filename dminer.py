from random import randint
"""
etat:
    0: vide
    1: bombe
    2: drapeau

"""

def generate_grid():
    grid = {}
    for colonne in range(1, 11):
        for ligne in range(1, 11):
            grid[(colonne, ligne)] = ["0", "0", False]  # [etat, nombre_de_mines_autour, discovered]
    return grid

grid = generate_grid()



"""création de 20 mines aléatoires"""

liste_position = []
mine = 0
while mine < 20:
    x=randint(1, 11)
    y=randint(1, 11)
    if [x,y] not in liste_position:
        liste_position.append((x,y))
        mine+=1
"""
print(liste_position)
"""
for i in range(20):
    [x,y] = liste_position[0]
    if liste_position[0] in grid:
        grid[(x,y)] = [-1, 0]
        liste_position.remove(liste_position[0])

grid = generate_grid()

print("------------- DEMINEUR ------------\n")
print("     1  2  3  4  5  6  7  8  9 ")
print("  --------------------------------")
print("")
