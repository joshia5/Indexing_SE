# This function takes in the websiteID which is the ID of an input document,
# the keyword as the variable word and the positions of each keyword as the
# variable wordPositions, and passes this information to the index data
# structure by calling in the function add_entry from the index.py file's
# Index class

def add_index(websiteID, word, wordPositions)

    Index::add_entry(Index, word, websiteID, wordPositions)
