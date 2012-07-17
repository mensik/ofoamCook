
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
    
    def getDefaultVariables(self, tModel):
        return []

    def __repr__(self):
        return self.family
 
class FoamFileHeader():
    def __init__(self):
        self.name = 'FoamFile'
        self.data = {}
        self.data['version'] = '2.0'
        self.data['format'] = 'ascii'

class FoamFile:
    def __init__(self, header):
        self.header = header       
        self.data = []

class Variable:
    def __init__(self, name):
        self.dimension = '[]'
        self.type = 'No type'
        self.name = name
        self.relaxFactor = 0.7
        self.resControl = 1e-3
    
    def __str__(self):
        ret = "\t class\t\t" + self.type + ";\n\t dimensions\t" + self.dimension + ";\n\t object \t" + self.name + ";\n" 
        return ret
        
class VecVolVariable(Variable):
    def __init__(self, name):
        Variable.__init__(self, name)
        self.type = 'volVectorField'
        
class SpeedVariable(VecVolVariable):
    def __init__(self, name='U'):
        VecVolVariable.__init__(self, name)
        self.dimension = '[0 1 -1 0 0 0 0]'

class ScaVolVariable(Variable):
    def __init__(self, name):
        Variable.__init__(self, name)
        self.type = 'volScalarField'
        
class PressureVariable(ScaVolVariable):
    def __init__(self, name='p'):
        ScaVolVariable.__init__(self, name)
        self.dimension = '[0 2 -2 0 0 0 0]'
        self.relaxFactor = 0.3

class TurbKineticEnergy(ScaVolVariable):
    def __init__(self, name='k'):
        ScaVolVariable.__init__(self, name)
        self.dimension = '[0 2 -2 0 0 0 0]'
        
class DisipationRatio(ScaVolVariable):
    def __init__(self, name='epsilon'):
        ScaVolVariable.__init__(self, name)
        self.dimension = '[0 2 -3 0 0 0 0]'
