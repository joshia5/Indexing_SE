'''
Dictionary containing word data for a website is
passed into the function. It then passes each word 
and its positions to the function add_index()
'''

def parseData(websiteWordData):
    websiteID = websiteWordData["website"]
    for word in websiteWordData["wordData"]: 
        wordPositions = websiteWordData["wordData"][word]
        add_index(websiteID, word, wordPositions)


file =  {
            "website": 1, 
            "wordData": {"word1": [1,2,3,4], "word2": [5,6,7,8]}
        }

parseData(file)
