#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Fichier main (exécution du code _ "serveur")

import game_link_db as gldb
import mouvement as mouv
import actions as act
import tkinter as tk
from tkinter import ttk

""" TO DO
creer les fonctions de déplacement
"""


root = tk.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
