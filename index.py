

class Index:
    def __init__(self):
        # data structure will be
        # {word:{doc_id:{positions}}}
        self.index = {}

    def add_entry(self, word, doc_id, positions=None):
        '''
        Adds a given entry to the inverted index

        Parameters
        ----------
        word : str
                word to index
        doc_id : int
                database id for document
        positions : set[int]
                locations of word in document

        Returns
        -------
        bool
                True if successful, False otherwise
        '''
        if positions is None or len(positions) == 0:
            return False
        if word in self.index:
            if doc_id in self.index[word]:
                # possibly update positions
                self.index[word][doc_id].union(positions)
            else:
                # add doc and positions
                self.index[word][doc_id] = positions
        else:
            # add new full entry
            self.index[word] = {}
            self.index[word][doc_id] = positions
        return True

    def remove_entry(self, word, doc_id=-1):
        '''
        Removes either the full entry or one
        document associated with the word if
        doc_id is specified

        Parameters
        ----------
        word : str
                word in index to remove associated data
        doc_id : int, optional
                database id for document to remove, if this
                is specified only this word, document pair is removed

        Returns
        -------
        dict or set
                Removed entry if successful, None otherwise
        '''
        entry = None
        if doc_id == -1:
            if word in self.index:
                # remove whole word
                entry = self.index.pop(word)
        else:
            if word in self.index and doc_id in self.index[word]:
                # remove only word-document pair
                entry = self.index[word].pop(doc_id)
        return entry

    def find_entry(self, word):
        '''
        Finds an entry in the inverted index
        and returns the result if entry is found

        Parameters
        ----------
        word : str
                word string to find in inverted index

        Returns
        -------
        dict
                dictionary containing document_ids to positions
                for this word
                None if not found
        '''
        entry = {}
        if word in self.index:
            entry = self.index[word]
        return entry
