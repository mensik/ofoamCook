import types
from cmdUtils import chooseFromList, setupFromOptions

class Header(types.FoamFileHeader):
    def __init__(self):
        types.FoamFileHeader.__init__(self)
        self.data['class'] = 'dictionary'
        self.data['location'] = '"constant"'
        self.data['object'] = 'RASProperties'

class Options:
    options = [('RASModel' , ['laminar', 'kEpsilon', 'kOmega', 'RNGkEpsilon', 'realizableKE', 'SpalartAllmaras', 'kOmegaSST']),
           ('turbulence' , ['on', 'off']),
           ('printCoefs' , ['on', 'off']),
           ('<RASModel>Coefs' , {})]
    
    modelCoefs = {'laminar' : {},
              'kEpsilon' : {'Cmu': 0.09, 'C1' : 1.44, 'C2' : 1.92, 'sigmaEps' : 1.3},
              'kOmega' : {'Cmu': 0.09, 'alpha' : 0.52, 'beta' : 0.072, 'alphaK' : 0.5, 'alphaOmega' : 0.5}
              }
    
def cmdSetup():
    RASPfile = types.FoamDictionaryFile(Header())
    
    for (option, values) in Options.options:
        if option != '<RASModel>Coefs':
            RASPfile.data[option] = chooseFromList('Choose ' + option + ' : ', values)
            
    RASPfile.data[RASPfile.data['RASModel'] + 'Coefs'] = setupFromOptions(Options.modelCoefs[RASPfile.data['RASModel']])
    
    return RASPfile
    
    
    
    
    
    
