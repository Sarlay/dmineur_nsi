from random import randint
"""
etat:
    0: vide
    -1: bombe
    -2: drapeau
"""

def generate_grid():
    grid = {}
    for colonne in range(1, 11):
        for ligne in range(1, 11):
            grid[(colonne, ligne)] = ["0", "0", False]  # [etat, nombre_de_mines_autour, discovered]
    return grid


"""création de 20 mines aléatoires"""
def generate_mines():
    liste_position = []
    mine = 0
    while mine < 20:
        x=randint(1, 10)
        y=randint(1, 10)
        if (x,y) not in liste_position:
            liste_position.append((x,y))
            mine+=1
    return liste_position

"""
print(liste_position)
"""
def add_mines_to_grid(liste_position, grid):
    for i in range(20):
        if liste_position[0] in grid:
            [x,y] = liste_position[0]
            grid[(x,y)] = ["-1", "0", False]
            liste_position.remove(liste_position[0])
    return grid

            
            

def calculate_near_sum(coo, grid):
    near_sum = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x != 0 or y != 0:
                if grid[(int(coo[0]-x), coo[1]-y)][0] == "-1":
                   print(f"true, in {x}, {y}")
                   near_sum += 1
    return near_sum
            

    
def show_debug_grid(grid):
    print("""
====    grille secrète:  ====
""")
    print("      1  2  3  4  5  6  7  8  9  10")
    print("    ________________________________")
    for x in range(1, 11):
        if x == 10: ## for the last line
            print(f"{x} | ", end="")  # remove a space because of the 2 digits causing line shift 
        else:
            print(f"{x}  | ", end="") 
        for y in range(1, 11):
            type_element = grid[(x, y)][0]
            if type_element.startswith("-") is False:
                type_element = " " + type_element  # fixes '-' line shift
            print(type_element, end=" ")
        print("|") # closes the right side of the grid
    print("    --------------------------------")
'''
def generate_grid_player():
    grid_player = {}
    for colonnex in range(1, 11):
        for ligney in range(1, 11):
            grid[(colonnex, ligney)] = ["."]  
    return grid_player
'''
list_cases = []
for nb in range(101):
    list_cases.append(".")
    

choix_joueur = int(input("Que voulez vous faire ?, découvrir une case: 1 ; planter un drapeau: 2"))
xpoint = []
ypoint = []
if choix_joueur = 1:
    if 1 < positionx_joueur and positiony_joueur < 10:
        positionx_joueur = int(input("saisissez l'abscisse de la case"))
        positiony_joueur = int(input("saisissez l'ordonnée de la case"))
        grid[(xpoint)] = [positionx_joueur]
        grid[(ypoint)] = [positiony_joueur]
else:
    positionx_drapeau = int(input("saisissez l'abscisse de la case"))
    positiony_drapeau = int(input("saisissez l'ordonnée de la case"))
    if 1 < positionx_drapeau and positiony_drapeau < 10:
        
      
print("""
====    grille secrète:  ====
""")
print("      1  2  3  4  5  6  7  8  9  10")
print("    ________________________________")


grid_player = generate_grid_player()
grid = generate_grid()
liste_position = generate_mines()
add_mines_to_grid(liste_position, grid)
