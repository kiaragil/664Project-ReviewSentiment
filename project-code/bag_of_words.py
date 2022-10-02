import os
from collections import Counter

# n denotes  how many files we want to look at
n = 1300

# directory = 'aclImdb/test/neg/'

# for filename in os.listdir(directory)[:n]:
#     f = os.path.join(directory, filename)
#     # checking if it is a file
#     if os.path.isfile(f):
#         #if so do...
#         print("START ---------\n")
#         freq_words(f)
#         print("--------- END\n\n")

 
c, directory = Counter(), 'aclImdb/test/neg/'

# iterate thru filenames in a specified folder
for filename in os.listdir(directory)[:n]:
    fname = os.path.join(directory, filename)
    if os.path.isfile(fname):
        with open(fname) as f:
            c += Counter(f.read().split())
            
# print words and freq
for word in c.most_common(50):
    print(word)
