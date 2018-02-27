class FileManager:

    def __init__(self):
        self.fileHandle = None


    # def setHendler(self, fileHandle):
    #     self.fileHandle = fileHandle

    def openFile(self, filename, mode="r"):
        self.fileHandle = open(filename, mode)

    def readFile(self):
        print(self.fileHandle.readLines())


    def writeToFile(self):
        self.fileHandle.write("A totally new line")

    def closeFileHandler(self):
        self.fileHandle.close()


fileManager = FileManager()
fileManager.openFile("test.txt")
fileManager.readFile()

fileManager.openFile("test.txt", "a")
fileManager.writeToFile()

fileManager.openFile("test.txt")
fileManager.closeFileHandler()
