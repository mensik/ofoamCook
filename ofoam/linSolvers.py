import cmdUtils
from ofoam.cmdUtils import chooseFromList, setupFromOptions

class Options:
    options = {
    'PCG' : {
    
           'preconditioner' : ['DIC', 'FDIC', 'diagonal', 'none'],
           'tolerance' : 1e-7,
           'relTol' : 0.001
           },
    
    'PBiCG' : {
           'preconditioner' : ['DILU', 'diagonal', 'none'],
           'tolerance' : 1e-7,
           'relTol' : 0.001
           },
    
    'GAMG' : {
            'preconditioner' : ['DIC', 'FDIC', 'DILU', 'diagonal', 'GAMG', 'none'],
            ##@todo OTESTOVAT GAMG
            'mergeLevels' : 1,
            'smoother' : 'GaussSeidel',
            'aglomerator' : 'faceAreaPair',
            'nCellsInCoarsestLevel' : 100,
            'tolerance' : 1e-5,
            'relTol' : 0
            }
        }

def cmdSetup(vName):
    setup = {}
    print 'SETUP ' + vName
    setup['solver'] = chooseFromList('Select solver : ', Options.options.keys())
    setup.update(setupFromOptions(Options.options[setup['solver']]))
    
    return setup
    
    
