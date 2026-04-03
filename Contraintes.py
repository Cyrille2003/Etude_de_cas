import numpy as np
from pathlib import Path
import json
from Geometrie import r_int

from pathlib import Path
chemin = Path(__file__).parent / "resultats.json"

with open(chemin, encoding="utf-8") as fichier:
    data = json.load(fichier)

print(data)    
q = data["Q"]
print(q)
to_max = 60                     # À changer lorsqu'on aura trouvé to_max.
sigma_max = 50
def cisaillement_pur(V, Q, I, t):
    """
    V est l'effort tranchant.
    Q est le premier moment d'air
    I est le moment d'inertie de la section totale
    t est la largeur de la section
    """

    tho = V*Q/(I*t)
    return tho



def Pression_axiale(P, r, t):
    return P*r/(2*t)

def Pression_circonferentielle(P, r, t):
    return P*r/(t)


def cisaillement_combine(force, aire, *autres_params):
    contrainte = force/aire
    return contrainte


def flexion_pure(force, aire):
    contrainte = force/aire
    return contrainte


def compression(force, aire):
    contrainte = force / aire
    return contrainte


def Config_1():
    cisaillement = 3
    cisaillement = cisaillement, to_max/cisaillement
    normale = 4
    normale = normale, sigma_max / normale
    return cisaillement, normale

def Config_2():
    cisaillement = 3
    cisaillement = cisaillement, to_max/cisaillement
    normale = 4
    normale = normale, sigma_max / normale
    return cisaillement, normale

def Config_3():
    cisaillement = 3
    cisaillement = cisaillement, to_max/cisaillement
    normale = 4
    normale = normale, sigma_max / normale
    return cisaillement, normale

def Config_4():
    cisaillement = 3
    cisaillement = cisaillement, to_max/cisaillement
    normale = 4
    normale = normale, sigma_max / normale
    return cisaillement, normale




chemin = Path(__file__).parent / "ETATS.json"
with open (chemin, mode="w", encoding="utf-8") as fichier:
    res = {"1":Config_1(), "2":Config_2(), "3":Config_3(), "4":Config_4()}
    json.dump(res, fichier, indent=4)
    print("Les résultats pour les différentes configurations ont été consignés dans le fichier JSON")