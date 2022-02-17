from random import randint
from tkinter import *


def generate_grid():  # Raphael
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


def generate_mines():  # cleante
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


def add_mines_to_grid(liste_position, grid): # cleante
    for i in range(20):
        if liste_position[0] in grid:
            [x,y] = liste_position[0]
            grid[(x,y)] = ["-1", "0", False]
            liste_position.remove(liste_position[0])
    return grid


def calculate_near_sum(coo, grid): # Raphael
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

    
def show_debug_grid(grid):  # Raphael
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


def show_player_grid(grid):  # Cleante
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
            if grid[(x, y)][1] is True: # if flag is placed here 
                print(" #", end=" ")
            elif grid[(x, y)][2] is True: # when the element is discovered by the player it displays it
                print(" " + str(calculate_near_sum((x, y), grid)), end=" ") 
            else:
                print(" .", end=" ") 
        print("|") 
    print("    --------------------------------")


def check_if_coordinate_valid(positionx, positiony):  # cleante
    if 1 <= positionx <= 10 and 1 <= positiony <= 10:
        return True
    else:
        return False

def get_coordinates(): # Raphael
    positionx = int(input("saisissez l'abscisse de la case: "))   
    positiony = int(input("saisissez l'ordonnée de la case: ")) 
    return positionx, positiony


def interact_case(): # Raphael
    positionx, positiony = get_coordinates()
    coo_valid = check_if_coordinate_valid(positionx, positiony)
    print(coo_valid)
    if coo_valid and grid[(positionx, positiony)][2] is False:  # if case not discovered yet 
        if grid[(positionx, positiony)][0] == "-1": # if the case is a mine  
            print("BOOM !")
            exit()
        else:
            grid[(positionx, positiony)][2] = True  # mark the case as discovered 
    else:
        if coo_valid is False:
            print("Coordonees invalides !! Veuillez entrer des coordonees corrects")
        
        else:
            print("Case déja découverte Veuillez choisir une autre case !")


def interact_flag(): # Cleante
    positionx, positiony = get_coordinates()
    coo_valid = check_if_coordinate_valid(positionx, positiony)
    interaction_type = input("Voulez vous ajouter (a) ou supprimer (s) un drappeau ? (a/s): ") 
    if coo_valid and interaction_type == "a":
        grid[(positionx, positiony)][1] = True  # add flag to the case at positionx, positiony coordinates
    elif coo_valid and interaction_type == "s":
        grid[(positionx, positiony)][1] = False  # add flag to the case at positionx, positiony coordinates
    else:
        if coo_valid is False:
            print("Coordonees invalides !! Veuillez entrer des coordonees corrects")
        
        else:
            print("Case déja découver, Veuillez choisir une autre case !")


def get_highest_score(): # Cleante
    score_file = open('highest_score.txt','r')
    score = score_file.read()
    score_file.close()
    if score != "":
        return int(score)
    else:
        return 0

# the main function

grid = generate_grid()
liste_position = generate_mines()
add_mines_to_grid(liste_position, grid)

highest_score = get_highest_score()

case_valid = 0

while True:
    show_player_grid(grid)
    if case_valid > highest_score:
        print("Nouveau record battu ! le score de {case_valid} est atteint")
    choix_joueur = str(input("Que voulez vous faire ?,\ndécouvrir une case: c ; planter un drapeau: d\n")) 
    if choix_joueur == "c": 
        interact_case()
        case_valid += 1
    elif choix_joueur == "d":
        interact_flag()
    elif choix_joueur == "NSI":  
        show_debug_grid(grid) 
