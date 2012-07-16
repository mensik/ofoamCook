from ..types import ASolver

class Incompressible(ASolver): 
    def __init__(self):
        self.family = 'incompressible'
    

class IcoFoam(Incompressible):
    pass
        