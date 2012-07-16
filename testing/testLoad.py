import ofoam

problem = ofoam.Problem()
problem.loadBoundaries()

writer = ofoam.fileUtils.FileWriter('testFile')
writer.writeNestedDictionaries('boundaries', problem.boundaries.data)
writer.close()
