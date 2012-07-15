import fileParser
import boundaries

class Problem:
	
	def loadBoundaries(self):
		self.boundaries = fileParser.parseBounds()
