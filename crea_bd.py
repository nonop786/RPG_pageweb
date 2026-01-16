import sqlite3 as sql

def creer_bd():
    """
    CREATE DATABASE rpg;
    USE rpg;
    """
    return None

""" Utilisable une fois la bd créé """
connexion = sql.connect("rpg.bd")
cursor = connexion.cursor()

def creer_table(): 
    cursor.execute("CREATE Table joueurs(identifiant INT PRIMARY KEY NOT NULL,pseudo VARCHAR,email VARCHAR,mdp VARCHAR);")
    print("table joueur fait !")
    cursor.execute("CREATE Table perso(identifiant INT REFERENCES joueurs(identifiant),niveau INT,objects VARCHAR,position_x INT,position_y INT,Poids_max INT,monnaie INT,statistique_id INT REFERENCES statistique(identifiant));")
    print("table perso fait !")
    cursor.execute("CREATE Table inventaire(identifiant INT REFERENCES joueurs(identifiant),nom_obj VARCHAR REFERENCES objets(nom),quantites INT,poids_inv INT);")
    print("table inventaire fait !")
    cursor.execute("CREATE Table statistique(identifiant INT PRIMARY KEY,degats INT,coup_crit INT,type_attaque INT,vitesse_dep INT,vitesse_attaque INT,vie INT,resist_mag INT,resist_phy INT);")
    print("table statistique fait !")
    cursor.execute("CREATE Table objets(nom VARCHAR PRIMARY KEY,degat INT,coup_crit INT,type_attaque INT,vitesse_dep INT,vitesse_attaque INT,vie INT,resist_mag INT,resist_phy INT);")
    print("table objets fait !")
    cursor.execute("CREATE Table monstres(nom VARCHAR,identifiant_stat INT REFERENCES statistique(identifiant));")
    print("table monstres fait !")
    print("c'est finit !")
    return None 

#creer_table()

def initialisation():
    """
    But : remplire les tables avec les données minimum du jeu (stats / monstres / objets /comptes dev -> auto set des perso)
    """
    return print("remplissage primaire des tables finit.")

"""
CREATE Table joueurs(identifiant INT PRIMARY KEY NOT NULL,
                     pseudo VARCHAR,
                     email VARCHAR,
                     mdp VARCHAR);

CREATE Table perso(identifiant INT REFERENCES joueurs(identifiant),
                   niveau INT,
                   objects VARCHAR,
                   position_x INT,
                   position_y INT,
                   Poids_max INT,
                   monnaie INT,
                   statistique_id INT REFERENCES statistique(identifiant));

CREATE Table inventaire(identifiant INT REFERENCES joueurs(identifiant),
                        nom_obj VARCHAR REFERENCES objets(nom),
                        quantites INT,
                        poids_inv INT);

CREATE Table statistique(identifiant INT PRIMARY KEY,
                         degats INT,
                         coup_crit INT,
                         type_attaque INT,
                         vitesse_dep INT,
                         vitesse_attaque INT,
                         vie INT,
                         resist_mag INT,
                         resist_phy INT);


CREATE Table objets(nom VARCHAR PRIMARY KEY,
                    degat INT,
                    coup_crit INT,
                    type_attaque INT,
                    vitesse_dep INT,
                    vitesse_attaque INT,
                    vie INT,
                    resist_mag INT,
                    resist_phy INT);

CREATE Table monstres(nom VARCHAR, 
                      identifiant_stat INT REFERENCES statistique(identifiant));

"""
