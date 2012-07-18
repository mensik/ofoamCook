import re
import types

## Class providing functionality for parsing OpenFOAM files
#
## @author Martin Mensik
class FileParser:

    ## @param lines list of lines in file
    ## @param pos starting position in file  
    def __init__(self, lines, pos=0):
        self.lines = lines
        self.pos = pos
    
    ## Returns the current line
    ## @return current line
    def getLine(self, stripped=True):
        line = self.lines[self.pos]
        if stripped:
            line = line.strip()
        return line
    
    ## Moves the current position in the file
    # @param noLines number of lines to move
    def move(self, noLines=1):
        self.pos = self.pos + noLines
    
    ## Finds the line containing the requested regular expression
    #
    # Moves the current file position on the requested line
    #
    ## @param key regular expression to look for
    ## @param fromBegining forces search to start at the begining of the file
    def findLine(self, key, fromBegining=False):
        if fromBegining:
            self.pos = 0
        
        while re.search(key, self.getLine()) == None:
            self.move()
    
    ## Reads keyword and entries on the current line
    #
    # Reads the current line. The first entry is key and the second is value. Then enters
    # this pair into the d.
    #
    ## @param d dictionary to store the entries in 
    def readKeyWord(self, d):
        prop = re.split('\W+', self.getLine())
        d[prop[0]] = prop[1]

    ## Reads directory 
    #
    # The function reads the directory structure that starts at the current line of the file.
    # The first line is the name of directory, in the following brackets is contained a list of key-value pairs.
    #
    ## @return tuple (name, entries)
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

class FileWriter:
    def __init__(self, fileName, mode='w'):
        self.file = open(fileName, mode)
        
    def close(self):
        self.file.close()
    
    def writeOptions(self, oname, opts, nTab = 0):
        if oname != None:
            self.file.write('\n' + nTab*'\t' + oname + "\n" + nTab*'\t' +"{\n")
        
        for (name, value) in opts:
            
            if isinstance(value, list):
                FileWriter.writeOptions(self, name, value, nTab+1)
            else:
                self.file.write(nTab*'\t' + "\t" + name + "\t\t" + str(value) + ";\n")

        if oname != None:
            self.file.write(nTab*'\t' + "}\n")
            
    def writeHeader(self):
        
        head = '''
/*
            ______                      ______            __  
     ____  / ____/___  ____ _____ ___  / ____/___  ____  / /__
    / __ \/ /_  / __ \/ __ `/ __ `__ \/ /   / __ \/ __ \/ //_/
   / /_/ / __/ / /_/ / /_/ / / / / / / /___/ /_/ / /_/ / ,<   
   \____/_/    \____/\__,_/_/ /_/ /_/\____/\____/\____/_/|_|
*/                                                          
        '''
        self.file.write(head);
        
def saveFoamFile(foamFile, fileName):
    writer = FileWriter(fileName)
    
    writer.writeHeader()
    writer.writeOptions('FoamFile', foamFile.header.data)
    
    for (name, opts) in foamFile.data:
        writer.writeOptions(name, opts)
    
    writer.close()
    