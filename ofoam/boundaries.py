types = ('patch', # The basic patch type for a patch condition that contains no geometric or topological 
                  # information about the mesh (with the exception of wall), e.g. an inlet or an outlet.
         'wall',
         'empty',
         'symetryPlane',
         'wedge',
         'cyclic',
         'processor')

from fileUtils import FileParser

class Boundaries:
    def __init__(self):
        self.data = parseBounds()
        
    def __repr__(self):
        repString = "Boundary\t\tTYPE\n-----------------------------------------\n"
        
        for (key, value) in self.data.iteritems():
            repString += key + "\t\t" + value['type'] + "\n"
        
        return repString + "\n"


## Parse file containing information about boundaries of a domain
def parseBounds(fileName='constant/polyMesh/boundary'):

    f = open(fileName, 'r')
    lines = f.readlines()
    pars = FileParser(lines)
    
    pars.findLine('FoamFile')
    fFile = pars.readDictionary()
    
    if fFile[1]['object'] != 'boundary':
        print 'Wrong file type!'

    bounds = pars.readNumberedList()
    
    return bounds


