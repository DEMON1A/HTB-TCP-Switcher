from os import path
from utils.errorMessages import showError

def commaParser(fileArgument):
    if "," in fileArgument:
        fileNames = fileArgument.split(",")

        for fileName in fileNames:
            if path.exists(fileName): pass
            else:
                showError(exceptionRule="Options Error" , Message=f"{fileName} Doesn't exists.")
                return False

        return fileNames
    else:
        if path.exists(fileArgument): return fileArgument
        else:
            showError(exceptionRule="Options Error" , Message=f"{fileArgument} Doesn't exists.")
            return False
