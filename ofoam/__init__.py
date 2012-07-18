import incompressible
import rasproperties
import linSolvers
import nLinSolvers
import boundaries
import exceptions
import fileUtils
import controlDic
import types

solvers = {'icoFoam': incompressible.IcoFoam,
		   'simpleFoam': incompressible.SimpleFoam}

## Basic class to store and manipulate information about OpenFOAM problem
class Problem:
	
	def __init__(self):
		self.boundaries = None
		self.solver = None
		self.variables = None
		
	## Loads boundaries from the constant/polyMesh directory 
	def loadBoundaries(self):
		self.boundaries = boundaries.Boundaries()
		
	def saveFvSolution(self):
		header = types.FoamFileHeader()
		header.data += [('class','dictionary'),
					('location','"system"'),
					('object','fvSolution')]
		
		ffile = types.FoamFile(header)
		ffile.data.append(('solver', [(v.name, v.solver) for v in self.variables]))
		ffile.data.append((self.solver.nlSolver, self.nlSolverConf))
		ffile.data.append(('relaxationFactors', [(v.name, v.relaxFactor) for v in self.variables]))
		
		fileUtils.saveFoamFile(ffile, 'system/fvSolution')
		
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
