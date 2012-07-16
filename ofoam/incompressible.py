from types import SpeedVariable, PressureVariable, ASolver

class Incompressible(ASolver): 
    def __init__(self):
        self.family = 'incompressible'
        
    def getDefaultVariables(self):
        return [SpeedVariable(), PressureVariable()]
    

class IcoFoam(Incompressible):
    def __init__(self):
        Incompressible.__init__(self)
        self.type = 'icoFoam'
    
        
