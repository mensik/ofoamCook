
from fileUtils import FileParser
from exceptions import IncompleteData

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

    bounds = None
    try:
        f = open(fileName, 'r')
        lines = f.readlines()
        pars = FileParser(lines)
        
        pars.findLine('FoamFile')
        fFile = pars.readDictionary()
        
        if fFile[1]['object'] != 'boundary':
            raise IncompleteData('Wrong data file! Not object "boundary" but "' + fFile[1]['object'] + '"')
    
        bounds = pars.readNumberedList()
    except IncompleteData as e:
        raise e
    except:
        raise IncompleteData('Boundary file is corrupted or missing')
    
    return bounds


