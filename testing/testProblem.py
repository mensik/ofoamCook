import ofoam

prb = ofoam.Problem()
prb.loadBoundaries()

ofoam.solvers.incompressible.IcoFoam()

print prb

solv = ofoam.solvers.incompressible.IcoFoam()
print solv