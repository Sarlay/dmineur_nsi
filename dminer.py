from random import randint


def generate_grid():
    """Generate the grid
    type:
     0: empty
    -1: mine
    -2: flag
    """

    grid = {}
    for colonne in range(1, 11):
        for ligne in range(1, 11):
            grid[(colonne, ligne)] = ["0", "0", False, False]  # [type, number_of_mines_surronding, discovered]
    return grid



def generate_mines():
    """create the position of 20 random mines"""
    liste_position = []
    mine = 0
    while mine < 20:
        x=randint(1, 10)
        y=randint(1, 10)
        if (x,y) not in liste_position:
            liste_position.append((x,y))
            mine+=1
    return liste_position


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
                try:
                    if grid[(int(coo[0]-x), coo[1]-y)][0] == "-1":
                        near_sum += 1
                except:
                    pass
    return near_sum

    
def show_debug_grid(grid):
    print("""
====    grille secrète:  ====
""")
    print("      1  2  3  4  5  6  7  8  9  10")
    print("    ________________________________")
    for y in range(1, 11):
        if y == 10: ## for the last line
            print(f"{y} | ", end="")  # remove a space because of the 2 digits causing line shift 
        else:
            print(f"{y}  | ", end="") 
        for x in range(1, 11):
            type_element = grid[(x, y)][0]
            if type_element.startswith("-") is False:
                type_element = " " + type_element  # fixes '-' line shift
            print(type_element, end=" ")
        print("|") # closes the right side of the grid
    print("    --------------------------------")



def show_player_grid(grid):
    """Prints the player grid"""
    print("""
====    grille démineur:  ====
""")
    print("      1  2  3  4  5  6  7  8  9  10")
    print("    ________________________________")
    for y in range(1, 11):
        if y == 10: ## for the last line
            print(f"{y} | ", end="")  # remove a space because of the 2 digits causing line shift 
        else:
            print(f"{y}  | ", end="")
        for x in range(1, 11):
            if grid[(x, y)][2] is True: # if element is discovered by player: print it
                print(" " + str(calculate_near_sum((x, y), grid)), end=" ")
            else:
                print(" .", end=" ")
        print("|") # closes the right side of the grid
    print("    --------------------------------")



def check_if_coordinate_valid(positionx_joueur, positiony_joueur):
    if 1 <= positionx_joueur <= 10 and 1 <= positiony_joueur <= 10:
        return True
    else:
        return False

# the main function

grid = generate_grid()
liste_position = generate_mines()
add_mines_to_grid(liste_position, grid)





while True:
    show_player_grid(grid)
    choix_joueur = str(input("Que voulez vous faire ?, découvrir une case: c ; planter un drapeau: d\n"))
    if choix_joueur == "c" or choix_joueur == "d":
        positionx_joueur = int(input("saisissez l'abscisse de la case: "))
        positiony_joueur = int(input("saisissez l'ordonnée de la case: "))
        if check_if_coordinate_valid:   # check if entry exists     
            if grid[(positionx_joueur, positiony_joueur)][2] is False:  # if case hasn't been discovered yet:
                if grid[(positionx_joueur, positiony_joueur)][0] == "-1":  # :
                    if choix_joueur == "c":
                        print("BOOM !")
                    else:  # the choice of the player is 'd'
                        grid[(positionx_joueur, positiony_joueur)][0] = "-2" # replace type of element with a flag at coordinates                     
                    grid[(positionx_joueur, positiony_joueur)][2] = True  # mark the case as discovered
                else:
                    print("pas de mine à cet endroit")
                    if choix_joueur == "d":
                        print("Pas de mine à cet endroit !")
                    grid[(positionx_joueur, positiony_joueur)][2] = True  # mark case a disovered
            else:
                print("case déjà découverte !")
        else:
            print("case invalide")
    elif choix_joueur == "nsi":
        show_debug_grid(grid)

