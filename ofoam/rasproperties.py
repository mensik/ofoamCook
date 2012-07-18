import types
from cmdUtils import chooseFromList, setupFromOptions
from ofoam.types import FoamFileHeader

class Options:
    options = [('RASModel' , ['laminar', 'kEpsilon', 'kOmega', 'RNGkEpsilon', 'realizableKE', 'SpalartAllmaras', 'kOmegaSST']),
           ('turbulence' , ['on', 'off']),
           ('printCoefs' , ['on', 'off']),
           ('<RASModel>Coefs' , {})]
    
    modelCoefs = {'laminar' : [],
              'kEpsilon' : [('Cmu', 0.09), ('C1' , 1.44), ('C2' , 1.92), ('sigmaEps' , 1.3)],
              'kOmega' : [('Cmu', 0.09), ('alpha' , 0.52), ('beta' , 0.072), ('alphaK' , 0.5), ('alphaOmega' , 0.5)]
              }
    
def cmdSetup():
    
    header = FoamFileHeader()
    header.data += [('class', 'dictionary'),
                    ('location', '"constant"'),
                    ('object', 'RASPProperties')]
    
    RASPfile = types.FoamFile(header)
    
    opts = []
    
    for (option, values) in Options.options:
        if option != '<RASModel>Coefs':
            opts.append((option, chooseFromList('Choose ' + option + ' : ', values)))
            
    opts.append((opts[0][1] + 'Coefs', setupFromOptions(Options.modelCoefs[opts[0][1]])))
    
    RASPfile.data.append((None, opts))
    return RASPfile
    
    
    
    
    
    
