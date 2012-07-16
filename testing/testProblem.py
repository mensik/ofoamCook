import ofoam
import general

prb = ofoam.Problem()
prb.loadBoundaries()

general.cmdUtils.editDictionary('B', prb.boundaries.data.values()[0])

ofoam.incompressible.IcoFoam()

print prb

solv = ofoam.incompressible.IcoFoam()
print solv