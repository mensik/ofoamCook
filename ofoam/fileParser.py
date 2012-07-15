import re

class FileParser:
    def __init__(self, lines, pos = 0):
        self.lines = lines
        self.pos = pos
    
    def getLine(self, stripped = True):
        line = self.lines[self.pos]
        if stripped:
            line = line.strip()
        return line
    
    def move(self, noLines = 1):
        self.pos = self.pos + noLines
        
    def findLine(self, key, fromBegining = False):
        if fromBegining:
            self.pos = 0
        
        while re.search(key, self.getLine()) == None:
            self.move()
    

def readKeyWord(line, dict):
    prop = re.split('\W+', line)
    dict[prop[0]] = prop[1]

def readDictionary(pars):
    name = pars.getLine()
    entries = {}
    pars.move(2)
        
    while pars.getLine() != '}':
        readKeyWord(pars.getLine(), entries)
        pars.move()
    return (name, entries)

def readNumberedList(pars):
    
    pars.findLine('[0-9]')
    
    nEntries = int(re.search('[0-9]*', pars.getLine()).group(0))
    pars.move(2)
    
    list = {}

    for i in range(nEntries):
        dic = readDictionary(pars)
        list[dic[0]] = dic[1] 
        pars.move()
    
    return list

def parseBounds(fileName='constant/polyMesh/boundary'):

    f = open(fileName, 'r')
    lines = f.readlines()
    pars = FileParser(lines)
    
    pars.findLine('FoamFile')
    fFile = readDictionary(pars)
    
    if fFile[1]['object'] != 'boundary':
        print 'Wrong file type!'

    bounds = readNumberedList(pars)
    
    return bounds
