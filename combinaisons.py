import numpy as np
from classe_reacteur import Reacteur, Circonferentiel, Axial
import pandas as pd
from itertools import product

combi = np.meshgrid([0,1,2], [-1,0,1], [0,1,2,3])
val_ax, val_fob, val_position = combi
# Reacs = Reacteur(axis=val_ax, fob=val_fob, position=val_position)

Reacs = [Reacteur(axis=a, fob=f, position=p) for a, f, p in product([0,1,2], [-1,0,1], [0,1,2,3])]

liste_reacs = []

for r in Reacs:
    if np.array_equal(np.abs(r.axis), np.array([1,0,0])) and np.array_equal(np.abs(r.position), np.array([1,0,0])):
        continue
    if np.array_equal(np.abs(r.axis), np.array([0,1,0])) and np.array_equal(np.abs(r.position), np.array([0,1,0])):
        continue
    if np.array_equal(np.abs(r.axis), np.array([0,0,0])):
        continue
    else:
        liste_reacs.append(r)

etats = [0,1]
combis = list(product(etats, repeat=16))

