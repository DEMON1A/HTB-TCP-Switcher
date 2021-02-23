import os , optparse
import concurrent.futures
from utils.filesParser import commaParser
from utils.filesReader import readFile
from utils.contentReplacer import replaceContent

def collectOptions():
    optionsParser = optparse.OptionParser()
    optionsParser.add_option("-f" , "--file" , dest="file", default=False , help="The OpenVPN Config You Want To Switch")
    optionsParser.add_option("-o" , "--output" , dest="output" , default="configs" , help="The Directory That Contains The OpenVPN Config(s)")

    toolOptions,_ = optionsParser.parse_args()
    return toolOptions

def mainFunction(Options):
    fileOption = Options.file
    outputOption = Options.output

    filesStuff = commaParser(fileArgument=fileOption)

    if not filesStuff:
        pass
    elif type(filesStuff) == list:
        for singleFile in filesStuff:
            fileContent = readFile(singleFile)
            replaceContent(fileContent , outputOption , singleFile)
    else:
        fileContent = readFile(filesStuff)
        replaceContent(fileContent , outputOption , filesStuff)

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor() as optionsCollector:
        toolOptions = optionsCollector.submit(collectOptions)
        toolOptions = toolOptions.result()

    with concurrent.futures.ThreadPoolExecutor() as mainThreader:
        _ = mainThreader.submit(mainFunction , toolOptions)

# https://www.youtube.com/watch?v=Fp0BScQSSvg
# listen to MGK and chill dude.