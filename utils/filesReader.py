'''
this is just a comment because i hate writing functions at the top of the file
sorry for that lol, focus on the below code.
'''
from utils.errorMessages import showError

def readFile(filePath):
    fileContent = open(filePath , 'r')
    fileContent = fileContent.readlines()

    if len(fileContent) == 0:
        showError(exceptionRule="Reader Error" , Message=f"{filePath} is empty file")
        return False
    else:
        return fileContent