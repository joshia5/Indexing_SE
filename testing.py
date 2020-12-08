from index import *
def tests():
    test_count = 0
    index = Index()
    
    #adding an entry to an empty index
    if(index.add_entry("word1",1,{1,2,3,4}) == True):
        test_count = test_count + 1

    #adding an entry to an index that has the same doc_id as a previous entry
    if(index.add_entry("word2",1,{5,6,7,8}) == True):
        test_count = test_count + 1

    #adding an entry to an index that has a new doc_id and a new word
    if(index.add_entry("word3",2,{12,17,55}) == True):
        test_count = test_count + 1

    #adding an entry to an index that has a previously entered word but a different doc_id
    if(index.add_entry("word1",2,{122,171,255}) == True):
        test_count = test_count + 1

    if(index.add_entry("word3",3,{144,217,55}) == True):
        test_count = test_count + 1

    #adding an entry that has no positions (can't do it)
    if(index.add_entry("word4",1) == False):
        test_count = test_count + 1

    #adding an entry with a position set size of 0 (can't do it)
    if(index.add_entry("word4",2,{}) == False):
        test_count = test_count + 1

    #finding an entry that only appears in one document in the index
    if(index.find_entry("word2") == {1: {5, 6, 7, 8}}):
        test_count = test_count + 1

    #finding an entry that appears in multiple documents in the index
    if(index.find_entry("word1") == {1: {1, 2, 3, 4}, 2: {122, 171, 255}}):
        test_count = test_count + 1

    #removing an entry that only appears in one document from the index
    if(index.remove_entry("word2") == {1: {5, 6, 7, 8}}):
        test_count = test_count + 1

    #removing an entry that appears in multiple document from the index
    if(index.remove_entry("word3") == {2: {12, 17, 55}, 3: {144, 217, 55}}):
        test_count = test_count + 1

    #removing an entry with a specific doc_id from the index
    if(index.remove_entry("word1",2) == {122,171,255}):
        test_count = test_count + 1
    
    #after removing pa
    if(index.find_entry("word1") == {1: {1, 2, 3, 4}}):
        test_count = test_count + 1

    #removing an entry with a word that is present in the index but with a doc_id that is not (can't do it)
    if(index.remove_entry("word1",2) == None):
        test_count = test_count + 1

    #finding an entry that is not in the index from the index (can't do it)
    if(index.find_entry("word4") == None):
        test_count = test_count + 1

    #removing an entry that is not in the index from the index (can't do it)
    if(index.remove_entry("word4") == None):
        test_count = test_count + 1

    #removing an entry with a word that is not present in the index but with a doc_id that is (can't do it)
    if(index.remove_entry("word4",2) == None):
        test_count = test_count + 1

    #removing an entry with a word and doc_id that that aren't present in the index (can't do it)
    if(index.remove_entry("word4",55) == None):
        test_count = test_count + 1

    return test_count

print(tests())