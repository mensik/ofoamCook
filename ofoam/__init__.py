import fileParser
import types
import incompressible
import boundaries

## Basic class to store and manipulate information about OpenFOAM problem
class Problem:
	
	def __init__(self):
		self.boundaries = None
		self.solver = None
	
	## Loads boundaries from the constant/polyMesh directory 
	def loadBoundaries(self):
		self.boundaries = boundaries.Boundaries()
		
	def __repr__(self):
		repString = "  oFoamProblem STATUS\n=======================\n\n"
		
		if self.boundaries != None:
			repString += self.boundaries.__repr__()
		else:
			repString += "Boundaries : NOT SET \n\n"
			
		if self.solver != None:
			repString += self.solver.__repr__()
		else:
			repString += "Solver: NOT SET \n\n"
		
		
		
		return repString
