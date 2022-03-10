from random import randint
from tkinter import *
import colorama
from colorama import Fore, Back, Style

def generate_grid():  # Raphael
    """Generate the grid
    type:
     0: empty
    -1: mine
    """

    grid = {}
    for colonne in range(1, 11):
        for ligne in range(1, 11):
            grid[(colonne, ligne)] = ["0", False, False]  # [type, number_of_mines_surronding, discovered_bool]
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


def show_near_empty_cases(coo, grid): # Raphael
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x != 0 or y != 0:
                try:
                    if grid[(int(coo[0]-x), int(coo[1]-y))][0] == "0":
                        grid[(int(coo[0]-x), int(coo[1]-y))][2] = True
                except:
                    pass

    
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


def get_color_prefix(number): # Raphael
    if number == "1":
        return "\033[1;36;40m" # bright cyan
    if number == "2":
        return "\033[1;32;40m" # bright green
    if number == "3":
        return "\033[1;31;40m" # bright red
    if number == "4":
        return "\033[1;37;40m" # white
    else:
        return ""

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
                print("\033[1;33;40m #\033[0m", end=" ")
            elif grid[(x, y)][2] is True: # when the element is discovered by the player it displays it
                near_sum = str(calculate_near_sum((x,y), grid))
                print(" " + get_color_prefix(near_sum) + near_sum, end="\033[0m ") 
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


def interact_case(first_move, grid): # Raphael
    positionx, positiony = get_coordinates()
    coo_valid = check_if_coordinate_valid(positionx, positiony)
    coo = positionx, positiony
    if first_move is True: 
        show_near_empty_cases(coo, grid)
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


def interact_flag(grid): # Cleante
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
def play_game(pseudo = "Joueur"):
    grid = generate_grid()
    liste_position = generate_mines()
    add_mines_to_grid(liste_position, grid)

    highest_score = get_highest_score()
    first_move = True
    case_valid = 0

    while True:
        show_player_grid(grid)
        if case_valid > highest_score:
            print(f"Nouveau record battu {pseudo} ! le score de {case_valid} est atteint")
        choix_joueur = str(input("Que voulez vous faire ?,\ndécouvrir une case: c ; planter un drapeau: d\n")) 
        if choix_joueur == "c": 
            interact_case(first_move, grid)
            first_move = False
            case_valid += 1
        elif choix_joueur == "d":
            interact_flag(grid)
        elif choix_joueur == "NSI":  
            show_debug_grid(grid)
    

def Credit():
    print("""Créé par Sarlay et par Cléanteuh \n
          Créé avec la bibliothèque colorama, random et tkinter""")

  

username = None
exit_now = False
colorama.init()
while exit_now is not True:
    menu_ask = input("Que voulez vous faire ? Ecrivez JOUER pour lancer le jeu, Ecrivez CREDIT pour afficher les crédits, Ecrivez NOM pour changer de nom \n")
    if menu_ask == "NOM":
        username = input("Quel est votre pseudo ?")
    if menu_ask == "JOUER":
        if username is not None:
            play_game(username)
        else:
            play_game()
    if menu_ask == "CREDIT":
        Credit()
    
    
