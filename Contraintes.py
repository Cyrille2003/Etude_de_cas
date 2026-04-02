import numpy as np
from pathlib import Path
import json

from pathlib import Path
chemin = Path(__file__).parent / "resultats.json"

with open(chemin, encoding="utf-8") as fichier:
    data = json.load(fichier)

print(data)    
q = data["Q"]
print(q)
def cisaillement_pur(V, Q, I, t):
    """
    V est l'effort tranchant.
    Q est le premier moment d'air
    I est le moment d'inertie de la section totale
    t est la largeur de la section
    """

    tho = V*Q/(I*t)
    return tho

def cisaillement_combine(force, aire, *autres_params):
    pass


def flexion_pure(force, aire):
    pass


def compression(force, aire):
    res = force / aire
    return res


def Config_1():
    return 0

def Config_2():
    return 0


def Config_3():
    return 0


def Config_4():
    return 0, 0


chemin = Path(__file__).parent / "ETATS.json"
with open (chemin, mode="w", encoding="utf-8") as fichier:
    res = Config_1(), Config_2(), Config_3(), Config_4()
    json.dump(res, fichier, indent=4)
    print("Les résultats pour les différentes configurations ont été consignés dans le fichier JSON")