# This file contains the code and logic to perform
# proximity matching

# Step 1

  # Load the inverted indices in memory


# Step 2

  # load the inverted index into one object per input document


# Step 3

  # for each document,
  # sort the indices by their word positions in the document


# Step 4

  # take the number of words to look ahead in the proximity
  # matching as an argument to this function 
  # loop over the indices sorted by positions and if 
  # the difference in the position is 1 (the input argument) 
  # then those keywords will
  # be added to a list of proximity matched keywords

# Step 5

  # for a additional functionality, to perform proximity matching
  # within a window of size n, since this size n is a argument for
  # the function in step 4 we run the function above to  match
  # within a window of size n


