import ofoam
import unittest
import os

class ProblemTest(unittest.TestCase):
    
    problem = None
    
    def setUp(self):
        pass
    
    def testLoad(self):
        ProblemTest.problem = ofoam.Problem()
        ProblemTest.problem.loadBoundaries()
        print 'Loading OK'
        pass
    
    def testSave(self):
        writer = ofoam.fileUtils.FileWriter('testFile')
        writer.writeNestedDictionaries('Boundaries', ProblemTest.problem.boundaries.data)
        writer.close()
        os.remove('testFile')
        
        print 'Writing OK'
    
    def tearDown(self):
        pass

#writer = ofoam.fileUtils.FileWriter('testFile')
#writer.writeNestedDictionaries('boundaries', problem.boundaries.data)
#writer.close()
