import fileParser
import boundaries

## Basic class to store and manipulate information about OpenFOAM problem
class Problem:
	
	def loadBoundaries(self):
		self.boundaries = fileParser.parseBounds()
