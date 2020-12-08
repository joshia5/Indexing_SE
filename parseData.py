'''
Dictionary containing word data for a website is
passed into the function. It then passes each word 
and its positions to the function add_index()
'''


def parseData(websiteWordData, index):
    websiteID = websiteWordData["website"]
    for word in websiteWordData["wordData"]:
        wordPositions = websiteWordData["wordData"][word]
        index.add_entry(word, websiteID, wordPositions)


file = {
    "website": 1,
    "wordData": {"word1": [1, 2, 3, 4], "word2": [5, 6, 7, 8]}
}

# parseData(file)
