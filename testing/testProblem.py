import ofoam

prb = ofoam.Problem()
prb.loadBoundaries()

ofoam.incompressible.IcoFoam()

print prb

solv = ofoam.incompressible.IcoFoam()
print solv