# -*- coding: utf-8 -*-
"""
Pajani Arnaud _ 19/12/2025
Gestion de la BD
"""
connexion = sql.connect("rpg.bd")
cursor = connexion.cursor()


def recup_joueur(): 
    """
    permet d'obtenir les id, les pseudo des joueurs sous forme d'une liste de tuple
    """
    cursor.execute("SELECT identifiant, pseudo FROM joueurs")
    perso = cursor.fetchall()
    return perso # liste de tuple

def initialisation():
"""
But : remplire les tables avec les données minimum du jeu (stats / monstres / objets /comptes dev -> auto set des perso)
"""
    return print("remplissage primaire des tables finit.")
