#!/usr/bin/env python3

"""
Mastermind en Python
"""

import random
import pdb


def generer_combinaison(longueur_combinaison, etendue_combinaison):
    '''Créé combinaison en fonction de l'étendue et de la longueur voulue'''
    combinaison = []
    for i in range(longueur_combinaison):
        combinaison.append(random.randrange(etendue_combinaison))
    return combinaison


def recuperer_combinaison_joueur(longueur_combinaison):
    while True:
        try:
            print('Entrez vos chiffres séparés par des espaces')
            entree = input('>')
            combinaison_joueur = [int(x) for x in entree.split(' ')]
            difference_longueur = longueur_combinaison - len(combinaison_joueur)
            if difference_longueur:
                print('''Votre combinaison ne fait pas la même longueur '''
                      '''que la solution.''')
                print('Il y a %d chiffre(s) %s'  % (abs(difference_longueur), 'manquant(s).' if difference_longueur > 0 else 'en trop.'))
            else:
                break
        except:
            print('Vous avez rentré n\'importe quoi !!')
    return combinaison_joueur


def verification_placement(combinaison_joueur, solution):
    bien_places = 0
    mal_places = 0
    # Création de listes intermédiaires pour en retirer les bien placés
    inter_sol = solution.copy()
    inter_comb = combinaison_joueur.copy()

    for i in range(len(inter_sol)):
        if combinaison_joueur[i] == solution[i]:
            bien_places += 1
            inter_sol.remove(solution[i])
            inter_comb.remove(solution[i])

    solution = inter_sol.copy()
    combinaison_joueur = inter_comb.copy()
    #Compte les mal placés
    for i in inter_comb:
        try:
            inter_sol.remove(i)
            mal_places += 1
        except:
            pass
    return (bien_places, mal_places)


def test():
    longueur_combinaison = 5
    etendue_combinaison = 10
    solution = generer_combinaison(longueur_combinaison, etendue_combinaison)
    print(solution)
    combinaison_joueur = recuperer_combinaison_joueur(longueur_combinaison)
    print(combinaison_joueur)
    bien_places, mal_places = verification_placement(combinaison_joueur,
                                                      solution)
    print('Vous avez bien placé %d nombre(s) et mal placé %d' % (bien_places, mal_places))
    

def jouer():
    print('Combien voulez-vous avoir de chiffres à trouver ?')
    longueur_combinaison = int(input('>'))
    print('Quelle étendue de chiffres voulez-vous ?')
    etendue_combinaison = int(input('>'))
    play = True
    while play:
        solution = generer_combinaison(longueur_combinaison, etendue_combinaison)
        bien_places = 0
        while bien_places != longueur_combinaison:
            combinaison_joueur = recuperer_combinaison_joueur(longueur_combinaison)
            bien_places, mal_places = verification_placement(combinaison_joueur, solution)
            print('Vous avez bien placé %d nombre(s) et mal placé %d nombres.' % (bien_places, mal_places))
        print('Bravo ! Vous avez gagné !')
        print('Voulez-vous rejouer ? 0 pour non et n\'importe quoi d\'autre pour oui.')
        play = input('>')


jouer()
