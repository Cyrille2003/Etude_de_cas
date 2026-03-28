# Inertie du cercle
import numpy as np
import json
from pathlib import Path

def J_troue_non_polaire(c_ext, c_in):
    return np.pi / 4 * (c_ext**4 - c_in**4)

# l = module Lunaire
# s = module de Service.
epaisseur_s = 0.003
epaisseur_l = 0.0015
r_int = 0.8128 / 2
r_ext_l = r_int + epaisseur_l
r_ext_s = r_int + epaisseur_s
longueur_tunnel = 0.4064

I_lunaire = J_troue_non_polaire(r_ext_l, r_int)
I_service = J_troue_non_polaire(r_ext_s, r_int)

print(I_lunaire, I_service)

Aire_dune_section_l = np.pi * (r_ext_l**2 - r_int**2)            # en m2
Aire_dune_section_s = np.pi * (r_ext_s**2 - r_int**2)

Aire_interne_l = 2 * np.pi * r_int * longueur_tunnel
print(Aire_interne_l)

section_rectangulaire_centre = epaisseur_s * 2 * longueur_tunnel

Aire_disque_interne = np.pi * r_int**2

Q = Aire_dune_section_s / 2 * 4*(r_ext_s - r_int) / (3*np.pi)



def resultats():
    res = {"I_lunaire":I_lunaire, 
           "I_service":I_service, 
           "Aire_dune_section_l":Aire_dune_section_l,
           "Aire_dune_section_s":Aire_dune_section_s,
           "section_rectangulaire_centre":section_rectangulaire_centre,
           "Aire_disque_interne":Aire_disque_interne,
           "Q":Q
           }
    chemin = Path(__file__).parent / "resultats.json"
    
    with open (chemin, mode="w", encoding="utf-8") as fichier:
        json.dump(res, fichier, indent=4)
    print("resultats ont été consigné dans le fichier JSON")

resultats()

        
