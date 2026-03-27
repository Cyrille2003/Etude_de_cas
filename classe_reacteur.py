import numpy as np

F = 446             # 446 Newtons de force pour chaque réacteur
bras_levier_reacteur = 154/2 * 2.54 / 100               # en m.
rayon_cylindre = 36.8 / 2 * 2.54 / 100                  # en m.

class Reacteur:
    def __init__(self, 
                 axis:int,                      # Valeurs possibles : [0,1,2] = [x, y, z]
                 fob:int,                       # Forward - Backwards - Off. Valeurs possibles: [-1,0,1] = [avant, off, arriere]. Forward => le réacteur donne une force dans le sens positif de l'Axe sur lequel il est monté.
                 position:int):                 # Valeurs possibles : [0,1,2,3]      
        """
        axis : np.ndarray. C'est le vecteur unitaire de l'axe du réacteur.
        sens : booléen qui donne si on est dans le sens positif de l'axe ou dans le sens négatif
        actif : bool. Il donne si le réacteur est actif ou non.
        position : np.ndarray. Il donne l'axe sur lequel l'axe de propulsion est monté perpendiculairement.
        axis et position sont du genre np.array([0,0,1]) et np.array([1,0,0]). Donc ils n'ont qu'une seule composante non nulle.
        
        """
        # Est-ce que on pose un réacteur ou deux réacteurs par couple de réacteurs ?
        axis_vectors = np.array([[1,0,0], [0,1,0], [0,0,1]])
        self.axis = axis_vectors[axis]    


        self.axis = self.axis * fob

        position_vectors = np.array([[1,0,0], [0,1,0], [-1,0,0], [0,-1,0]])
        self.position = position_vectors[position]     
        
        
    def moment_cree(self, bras_de_levier=bras_levier_reacteur, force=F):           # Comme le réacteur principal de 91.2 kN ne crée pas de moment, on ne tient pas compte de son cas.
        amplitude = force * bras_de_levier               # Type : scalaire (float)
        direction = np.cross(self.axis, -self.position)     # Type : np.ndarray (vecteur unitaire à une seule composante)
        res = amplitude * direction                         # Type : np.ndarray (vecteur de norme F*bras_levier_reacteur)
        return res
    
    def force_cree(self, force=F):
        direction = self.axis
        amplitude = force
        res = amplitude * direction
        return res                                           # Type : np.ndarray
    
    def res(self):
        return [self.axis, self.force_cree(force=446), self.moment_cree()]      # Type : liste de np.ndarray
    
    def __str__(self):
        return f"{self.axis}, {self.position}"







class Circonferentiel(Reacteur):
    def __init__(self, axis, sens, actif, position):
        super.__init__(axis=axis,
                       sens=sens,
                       actif=actif,
                       position=position)
        
        
    

class Axial(Reacteur):
    def __init__(self, sens, actif, position):
        super.__init__(axis=np.ndarray([0,0,1]),
                       sens=sens,
                       actif=actif,
                       position=position)


