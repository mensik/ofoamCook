## Abstract solver prototype class
#
# This class and its subclasses are intended to serve as prototyping objects to
# initiate newly created solver configuration and to check the correct settings
#
class ASolver:
    def __init__(self):
        self.type = 'No type'
        self.family = 'No family'
        self.variables 
    
    def getDefaultVariables(self):
        return []

    def __repr__(self):
        return self.family
 
   
class Variable:
    def __init__(self):
        self.dimension = '[]'
        self.type = 'No type'
        self.name = 'No name'
    
    def __str__(self):
        ret = "\t class\t\t" + self.type + ";\n\t dimensions\t" + self.dimension + ";\n\t object \t" + self.name + ";\n" 
        return ret
        
class VecVolVariable(Variable):
    def __init__(self, name):
        self.name = name
        self.type = 'volVectorField'
        
class SpeedVariable(VecVolVariable):
    def __init__(self, name = 'U'):
        VecVolVariable.__init__(self, name)
        self.dimension = '[0 1 -1 0 0 0 0]'

class ScaVolVariable:
    def __init__(self, name):
        self.name = name
        self.type = 'volScalarField'
        
class PressureVariable(ScaVolVariable):
    def __init__(self, name = 'p'):
        ScaVolVariable.__init__(self, name)
        self.dimension = '[0 2 -2 0 0 0 0]'
        
        