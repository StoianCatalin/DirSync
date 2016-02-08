import os
import shutil

class Folder:
    def __init__(self, path):
        self.path = path

    def sync(self, toDir):
        "This method start sync of folders"
        filesList = os.listdir(self.path)
        self.deleteFile(toDir)
        for file in filesList:
            if(os.path.isdir(self.path + "/" + file)):
                os.mkdir(toDir + "/" + file)
                self.checkDir(self.path + "/" + file, toDir + "/" + file)
            else:
                if(os.path.isfile(self.path + "/" + file)):
                    shutil.copy2(self.path + "/" + file, toDir)

    def checkDir(self, dirPath, toDir):
        "This method create files for subdirectory"
        filesList = os.listdir(dirPath)
        for file in filesList:
            if(os.path.isdir(self.path + "/" + file)):
                os.mkdir(toDir + "/" + file)
                self.checkDir(toDir + "/" + file, toDir + "/" + file)
            else:
                if(os.path.isfile(self.path + "/" + file)):
                    shutil.copy2(self.path + "/" + file, toDir)

    def deleteFile(self, toDir):
        "This method remove all files that are not in source folder"
        fileList = os.listdir(toDir)
        for file in fileList:
            if(os.path.isdir(toDir + "/" + file)):
                shutil.rmtree(toDir + "/" + file)
            else:
                if(os.path.isfile(toDir + "/" + file)):
                    os.remove(toDir + "/" + file)