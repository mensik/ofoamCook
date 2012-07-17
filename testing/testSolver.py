import ofoam
from ofoam.fileUtils import saveFoamFile

raspFile = ofoam.rasproperties.cmdSetup()

saveFoamFile(raspFile, 'testFile2')