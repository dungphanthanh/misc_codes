import os

dirInput = "F:\\test\\in"
dirOutput = "F:\\test\\out"
searchFileExtension = ".ma"

searchString = "abc"
replaceString = "okokok"

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            filename, file_extension = os.path.splitext(fullPath)
            if file_extension==searchFileExtension:
                allFiles.append(fullPath)                
    return allFiles

for searchResult in getListOfFiles(dirInput):
    print searchResult
    print searchResult.split("\\")[-1]
    fIN = open(searchResult, "rt")
    fOUT = open(dirOutput+"\\"+searchResult.split("\\")[-1], "wt")

    for line in fIN:
        fOUT.write(line.replace(searchString, replaceString))

    fIN.close()
    fOUT.close()
