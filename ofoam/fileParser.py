def parseBound(fileName):
    
    bounds = {}

    import re

    f = open(fileName, 'r')
    
    lines = f.readlines()
    linePos = 0
    
    while lines[linePos].strip() != 'FoamFile':
        linePos = linePos + 1

    while lines[linePos].strip() != '}':
        linePos = linePos + 1
    
    while re.search('[0-9]', lines[linePos]) == None:
        linePos = linePos + 1

    noBoundaries = int(re.search('[0-9]*', lines[linePos]).group(0))
    
    linePos = linePos + 2

    for i in range(noBoundaries):
        name = lines[linePos].strip()
        properties = {}
        linePos = linePos+2
        
        while lines[linePos].strip() != '}':
            prop = re.split('\W+',lines[linePos].strip())
            properties[prop[0]]=prop[1]

            linePos = linePos + 1
        
        bounds[name] = properties
        linePos = linePos + 1
    return bounds
