import re

## Class providing functionality for parsing OpenFOAM files
#
## @author Martin Mensik
class FileParser:

    ## @param lines list of lines in file
    ## @param pos starting position in file  
    def __init__(self, lines, pos = 0):
        self.lines = lines
        self.pos = pos
    
    ## Returns the current line
    ## @return current line
    def getLine(self, stripped = True):
        line = self.lines[self.pos]
        if stripped:
            line = line.strip()
        return line
    
    ## Moves the current position in the file
    # @param noLines number of lines to move
    def move(self, noLines = 1):
        self.pos = self.pos + noLines
    
    ## Finds the line containing the requested regular expression
    #
    # Moves the current file position on the requested line
    #
    ## @param key regular expression to look for
    ## @param fromBegining forces search to start at the begining of the file
    def findLine(self, key, fromBegining = False):
        if fromBegining:
            self.pos = 0
        
        while re.search(key, self.getLine()) == None:
            self.move()
    
    ## Reads keyword and entries on the current line
    #
    # Reads the current line. The first entry is key and the second is value. Then enters
    # this pair into the dict.
    #
    ## @param dict directory to store the entries in 
    def readKeyWord(self,dict):
        prop = re.split('\W+', self.getLine())
        dict[prop[0]] = prop[1]

    ## Reads directory 
    #
    # The function reads the directory structure that starts at the current line of the file.
    # The first line is the name of directory, in the following brackets is contained a list of key-value pairs.
    #
    ## @return touple (name, entries)
    def readDictionary(self):
        name = self.getLine()
        entries = {}
        self.move(2)
            
        while self.getLine() != '}':
            self.readKeyWord(entries)
            self.move()
        return (name, entries)
    
    ## Reads list with defined number of entries
    #
    # Each entry is dictionary!
    #
    ## @return dictionary of named dictionaries
    def readNumberedList(self):
        
        self.findLine('[0-9]')
        
        nEntries = int(re.search('[0-9]*', self.getLine()).group(0))
        self.move(2)
        
        list = {}
    
        for i in range(nEntries):
            dic = self.readDictionary()
            list[dic[0]] = dic[1] 
            self.move()
        
        return list
