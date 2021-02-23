'''
i love cats.
'''
from os import path, mkdir
from utils.errorMessages import showGood

def replaceContent(fileContent , outputFolder , filePath):
    mainList = []

    for singleLine in fileContent:
        singleLine = singleLine.rstrip('\n')

        if "<tls-auth>" in singleLine:
            addedLine = singleLine.replace('<tls-auth>' , '<tls-crypt>')
            mainList.append(addedLine)
        elif "</tls-auth>" in singleLine:
            addedLine = singleLine.replace('</tls-auth>' , '</tls-crypt>')
            mainList.append(addedLine)
        elif "1337" in singleLine:
            addedLine = singleLine.replace('1337' , '443')
            mainList.append(addedLine)
        elif "proto udp" in singleLine:
            addedLine = singleLine.replace('proto udp' , 'proto tcp')
            mainList.append(addedLine)
        else:
            addedLine = singleLine
            mainList.append(singleLine)

    outputFile = '\n'.join(mainList)

    if path.exists(outputFolder): pass
    else: mkdir(outputFolder)

    with open(f'{outputFolder}/{filePath}' , 'w') as configFile:
        configFile.write(outputFile)

    showGood(goodRule="Output Saved" , Message=f"The TCP Config Has Been Saved On {outputFolder}/{filePath}")