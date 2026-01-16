#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3 as sql

connexion = sql.connect("rpg.bd")
cursor = connexion.cursor()

def initialisation():
    """
    But : remplire les tables avec les données minimum du jeu (stats / monstres / objets /comptes dev -> auto set des perso)
    """
    return print("remplissage primaire des tables finit.")


""" Réalisation à l'initialisation de la bd pour voir si chaque table est correctement mise en place"""

def allrecup_joueur(): 
    """
    permet d'obtenir tout de la table joueurs sous forme d'une liste de tuple
    """
    cursor.execute("SELECT * FROM joueurs")
    joueurs = cursor.fetchall()
    return joueurs # liste de tuple

def allrecup_perso(): 
    """
    permet d'obtenir tout de la table perso sous forme d'une liste de tuple
    """
    cursor.execute("SELECT * FROM perso")
    perso = cursor.fetchall()
    return perso # liste de tuple

def allrecup_inventaire(): 
    """
    permet d'obtenir tout de la table inventaire sous forme d'une liste de tuple
    """
    cursor.execute("SELECT * FROM inventaire")
    inventaire = cursor.fetchall()
    return inventaire # liste de tuple

def allrecup_statistique(): 
    """
    permet d'obtenir tout de la table statistique sous forme d'une liste de tuple
    """
    cursor.execute("SELECT * FROM statistique")
    statistique = cursor.fetchall()
    return statistique # liste de tuple

def allrecup_objets(): 
    """
    permet d'obtenir tout de la table objets sous forme d'une liste de tuple
    """
    cursor.execute("SELECT * FROM objets")
    objets = cursor.fetchall()
    return objets # liste de tuple

def allrecup_monstres(): 
    """
    permet d'obtenir tout de la table monstres sous forme d'une liste de tuple
    """
    cursor.execute("SELECT * FROM monstres")
    monstres = cursor.fetchall()
    return monstres # liste de tuple

print(allrecup_joueur())
print(allrecup_perso())
print(allrecup_inventaire())
print(allrecup_statistique())
print(allrecup_inventaire())
print(allrecup_inventaire())
