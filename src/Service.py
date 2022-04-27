import random,json,os
import time

list = ["Success", "Failed"]
dataDir = "D:\Shoukat\learning\SparkStreaming\SparkStreamingIDEA\PythonRESTService\data"

def readFile(filePath):

    with open(filePath, 'r') as openfile:
        json_object = json.load(openfile)
        return json_object

def runEngine (dirPath):

    directory = os.fsencode(dirPath)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print(filename)
        if filename.endswith(".new") :
            data = readFile(dirPath+"/"+filename)
            print(" ** Data ** ", data)
            os.rename(dirPath+"/"+filename, dirPath+"/"+filename+".precessing")
            time.sleep(2)

        else:
            print("No New files to process")


### Infinite Loop

while True:
    runEngine(dataDir)
    time.sleep(30)