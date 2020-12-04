import json

def parseData():
    # Opening JSON file 
    f = open('doc1_info.json', "r") 

    # returns JSON object as a dictionary 
    data = json.loads(f.read())

    # Take data from json file and add to dictionary
    websiteWordData = {}
    for i in data: 
        websiteWordData[i] = data[i]

    # Closing file 
    f.close()

    return websiteWordData

parseData()