from ofoam.cmdUtils import setupFromOptions
class Options:
    options = {
               'startFrom' : ['firstTime', 'startTime', 'latestTime'],
               'startTime' : 0,
               'stopAt' : ['endTime' , 'writeNow', 'noWriteNow', 'nextWrite'],
               'endTime' : 0.5,
               'deltaT' : 0.1,
               'writeControl' : ['timeStep', 'runTime', 'adjustableRunTime','cpuTime','clockTime'],
               'writeInterval' : 0.1,
               'purgeWrite' : 0,
               'writeFormat' : ['ascii', 'binary'],
               'writePrecision' : 6,
               'writeCompression' : ['uncompressed', 'compressed'],
               'timeFormat' : ['fixed', 'scientific','general'],
               'timePrecision' : 6,
               'graphFormat' : ['raw', 'gnuplot', 'xmgr', 'jplot']
               }
    
def cmdSetup(solverName):
    conf = {'application': solverName}
    conf.update(setupFromOptions(Options.options))
    return conf