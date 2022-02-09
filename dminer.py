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
        [x,y] = liste_position[0]
        if liste_position[0] in grid:
            grid[(x,y)] = [-1, 0]
            liste_position.remove(liste_position[0])

            
            

def calculate_near_sum(coo, grid):
    near_sum = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x != 0 or y != 0:
                if grid[(int(coo[0]-x), coo[1]-y)][0] == 1:
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



grid = generate_grid()
liste_position = generate_mines()
add_mines_to_grid(liste_position, grid)




print("------------- DEMINEUR ------------\n")
print("     1  2  3  4  5  6  7  8  9 ")
print("  --------------------------------")
print("")
