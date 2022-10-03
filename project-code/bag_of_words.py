import os
from collections import Counter

# n denotes  how many files we want to look at
n = 100

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

# for word in list(ArtofWarCounter):
#     if word in stop_list:
#         del c['word] 

stop_list = ['the','a', 'are','if','in','it','is', 'and',
            'about','of','or', 'i','than', 'have','this', 'that', 
            'from', 'which', 'did', 'to', 'by', 'we','/><br',
            'all', 'has', 'there', 'us', 'Mr.', 'for', 'was',
            'do', 'be', 'then', 'until', 'no', 'when', 'with', 
            'like', 'on', 'not', 'an', 'as', 'but', 'at', 'The',
            'At', 'just','they', 'so', 'out', 'his', 'her', 'you',
            'her', 'some', 'she', 'even', 'I', 'to']

# iterate thru filenames in a specified folder
for filename in os.listdir(directory)[:n]:
    fname = os.path.join(directory, filename)
    if os.path.isfile(fname):
        with open(fname) as f:
            words = Counter(f.read().split())
            for w in list(words):
                if w in stop_list:
                    del words[w]
                else:
                    c += words
                    
for word in c.most_common(50):
    print(word)
