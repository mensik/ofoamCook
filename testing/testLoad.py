import ofoam

problem = ofoam.Problem()
problem.loadBoundaries()

print problem.boundaries
