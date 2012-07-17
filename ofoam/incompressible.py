from types import SpeedVariable, PressureVariable, ASolver
from ofoam.types import TurbKineticEnergy, DisipationRatio

class Incompressible(ASolver): 
    
    variables = {
                 'laminar' : [SpeedVariable(), PressureVariable()],
                 'kEpsilon' : [SpeedVariable(), PressureVariable(), TurbKineticEnergy(), DisipationRatio()]
                 }
    
    def __init__(self):
        self.family = 'incompressible'
        
    def getDefaultVariables(self,turbulentModel):
        
        return Incompressible.variables[turbulentModel]
    

class IcoFoam(Incompressible):
    def __init__(self):
        Incompressible.__init__(self)
        self.type = 'icoFoam'

class SimpleFoam(Incompressible):
    def __init__(self):
        Incompressible.__init__(self)
        self.type = 'simpleFoam'
        
