import json

def parseData(jsonFile):
    # Opening JSON file 
    f = open(jsonFile, "r") 

    # returns JSON object as a dictionary 
    data = json.loads(f.read())

    # Take data from json file and add to dictionary
    websiteWordData = {}
    for i in data: 
        websiteWordData[i] = data[i]

    # Closing file 
    f.close()

    return websiteWordData

parseData('doc1_info.json')