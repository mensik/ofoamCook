import ofoam

raspFile = ofoam.rasproperties.cmdSetup()
writer = ofoam.fileUtils.FileWriter('testFile')
writer.writeDictionary(raspFile.header.name, raspFile.header.data)
writer.writeDictionary(None, raspFile.data)
writer.close()