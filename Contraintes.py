import numpy as np
from pathlib import Path
import json
from Geometrie import r_int, epaisseur_s, r_ext_s, longueur_tunnel

from pathlib import Path
chemin = Path(__file__).parent / "resultats.json"

with open(chemin, encoding="utf-8") as fichier:
    data = json.load(fichier)

print(data)    
q = data["Q"]
print(q)

E = 73.1e9                      
G = 27e9
to_max = 172e6                     # À changer lorsqu'on aura trouvé to_max.
sigma_max = 414e6                  # À changer.
bras_levier_reacteur = b_l = 154*0.0254/2
dist_reac_mur = (10*12 + 1) * 12 * 0.0254 + longueur_tunnel


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


def flexion_pure(Moment, position, I):
    contrainte_locale = Moment*position/I
    return contrainte_locale


def compression(force, aire):
    contrainte = force / aire
    return contrainte

def cisaillement_de_torsion(T, rho, J):
    return T*rho/J


def Config_1():
    """
    Figure 1 dans le rapport : compression maximale avec tous les réacteurs activés dans la même direction.
    """
    cisaillement = 0
    cisaillement = 0, "-"
    normale_circonférentielle = Pression_circonferentielle(34.5e3, r_int, epaisseur_s)
    normale = compression(force=91.2e3+446*4, aire=data["Aire_dune_section_s"]) - Pression_axiale(34.5e3, r_int, epaisseur_s)
    normale = max(normale, normale_circonférentielle)
    facteur_sec = sigma_max/normale
    normale_sortie = round(normale/1e6, 2), round(facteur_sec, 2)
    return cisaillement, normale_sortie

def Config_2():
    """
    Torsion maximale, Figure 2 dans le rapport.
    """
    cisaillement = cisaillement_de_torsion(T = 446*4*b_l, rho = r_ext_s, J=data["J_service"])
    cisaillement = round(cisaillement/1e6, 2), round(to_max/cisaillement, 2)
    normale = 0
    normale = normale, "-"
    return cisaillement, normale

def Config_3():
    """
    Contrôle d'attitude axiale (réorientation de l'axe.)
    On ajoute le réacteur principal pour maximiser la compression. (On étudie la compression sur une section annulaire.)
    
    Autrement dit, pour la normale maximale, 
    on prend la contrainte normale liée au Réacteur Principal, 
    plus la contrainte normale liée à la flexion, 
    moins la pression axiale
    
    (On étudie aussi le cisaillement présent dans une coupe rectangulaire axiale.)
    On multiplie la force par la racine de 2 parce qu'il faut tenir compte de l'orientation combinée des vecteurs.
    """
    force = np.sqrt(2) * 446
    cisaillement = cisaillement_pur(V=force, Q = data["Q_rect_s"], I=data["I_rect_s"], t=2*epaisseur_s)
    cisaillement = round(cisaillement/1e6, 2), round(to_max/cisaillement, 2)
    normale = flexion_pure(Moment=446*2*b_l, position=r_ext_s, I=data["I_service"]) + compression(91.2e3, data["Aire_dune_section_s"]) - Pression_axiale(34.5e3, r_int, epaisseur_s)
    facteur_sec = sigma_max / normale
    normale = round(normale/1e6, 2), round(facteur_sec, 2)
    return cisaillement, normale

def Config_4():
    """
    Ici, on a du cisaillement appliqué sur une section annulaire du cylindre.
    On a aussi de la compression due à la flexion.
    Pour la compression, on considérera la traction et on l'additionnera à la pression axiale. On aura donc une contrainte normale axiale maximale.
    La force maximale est 446*2 * (2*sqrt(2)). Justification : on réoriente les axes de sorte que les composantes verticales s'additionnent.
    """
    force = 2*np.sqrt(2)*446
    print(data["Q"])
    print(data["I_service"])
    print(2*epaisseur_s)
    cisaillement = cisaillement_pur(V=force, Q=data["Q"], I=data["I_service"], t= 2*epaisseur_s)
    print("CISAILLEMENT", cisaillement)
    facteur_sec_cis = to_max/cisaillement
    cisaillement = round(cisaillement/1e6, 4), round(facteur_sec_cis, 2)
    normale = flexion_pure(Moment=force*dist_reac_mur, position=r_ext_s, I=data["I_service"]) + Pression_axiale(P=34.5e3, r=r_int, t=epaisseur_s)
    facteur_sec_normale = sigma_max / normale
    normale = round(normale/1e6, 2), round(facteur_sec_normale, 2)
    return cisaillement, normale

def Petit_Tunnel():
    normale_max = max(Pression_axiale(P=34.5e3, r=r_int, t=0.0015), Pression_circonferentielle(P=34.5, r=r_int, t=0.0015))
    facteur_sec = sigma_max / normale_max
    normale = round(normale_max/1e6, 4), round(facteur_sec, 2)
    return normale


chemin = Path(__file__).parent / "ETATS.json"
with open (chemin, mode="w", encoding="utf-8") as fichier:
    res = {"1":Config_1(), "2":Config_2(), "3":Config_3(), "4":Config_4(), "Petit tunnel":Petit_Tunnel()}
    json.dump(res, fichier, indent=4)
    print("Les résultats pour les différentes configurations ont été consignés dans le fichier JSON")


print(3.14159/4*(.4094**4 - .4064**4))


print(np.pi*(r_ext_s**2 - r_int**2))