from random import randint
from os import chdir, getcwd
from colorama import Fore, Back, Style

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
        if y == 10: ## for print 10 lines
            print(f"{y} | ", end="")  
        else:                           ##remove a space because of the 2 digits causing a line shift
            print(f"{y}  | ", end="")
        for x in range(1, 11):
            if grid[(x, y)][2] is True: # when the element is discovered by the player it displays it
                print(" " + str(calculate_near_sum((x, y), grid)), end=" ") 
            elif grid[(x, y)][2] is None: # if he typed d the program therefore places a flag because d paces the last value of the dictionary in None
                print(" #", end=" ") 
            else:
                print(" .", end=" ") 
        print("|") 
    print("    --------------------------------")

# the main function


grid = generate_grid()
liste_position = generate_mines()
add_mines_to_grid(liste_position, grid)




def check_if_coordinate_valid(positionx_joueur, positiony_joueur):
    if 1 <= positionx_joueur <= 10 and 1 <= positiony_joueur <= 10:
        return True
    else:
        return False

case_valid = 0

while True:
    show_player_grid(grid)
    choix_joueur = str(input("Que voulez vous faire ?,\ndécouvrir une case: c ; planter un drapeau: d\n")) 
    if choix_joueur == "c" or choix_joueur == "d": 
        positionx_joueur = int(input("saisissez l'abscisse de la case: "))   
        positiony_joueur = int(input("saisissez l'ordonnée de la case: ")) 
        if check_if_coordinate_valid:       
            if grid[(positionx_joueur, positiony_joueur)][2] is False:  
                if choix_joueur == "c": 
                    if grid[(positionx_joueur, positiony_joueur)][0] == "-1":   
                        print('BOOM !, ton score est de", case_valid, "points')
                        print_score=(input("voulez vous enregistrer votre score ?, répondez par OUI ou NON"))
                        if print_score == "OUI":
                            obFichier=open('Score_Démineur.txt','a')
                            obFichier.write(str(case_valid))
                            obFichier.close()
                        else:
                            exit()
                    grid[(positionx_joueur, positiony_joueur)][2] = True 
                    case_valid+=1 
                if choix_joueur == "d": 
                    grid[(positionx_joueur, positiony_joueur)][2] = None 
                    grid[(positionx_joueur, positiony_joueur)][0] == "-2" 
            else:
                print("Ca marche pas frr") 
        else:
            print("case invalide !") 
    if choix_joueur == "NSI":  
        show_debug_grid(grid) 
    elif case_valid == 5:
        print("GG tu as survecu à cette torture")
        exit()


