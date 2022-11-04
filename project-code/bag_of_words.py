from multiprocessing.resource_sharer import stop
import os
import statistics
from collections import Counter
import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('universal_tagset')
nltk.download('stoplist')

def remove_punc(word):
    punc = '''-!()[]{};:"\,<>./?@#$%^&*_~'''
    no_punc_word = word.translate(str.maketrans('', '', punc))
    return no_punc_word

def make_lower(word):
    return word.lower()

def remove_words(lst):
    for word in lst:
        if word not in stop_list:
            words_final.append(word)

def word_count(fname):
    number_of_words = 0
    
    # Opening our text file in read only
    # mode using the open() function
    with open(fname, encoding="utf8") as file:
    
        # Reading the content of the file
        data = file.read()
    
        # Splitting the data into separate lines
        lines = data.split()
    
        # Adding the length of the
        # lines in our number_of_words
        number_of_words += len(lines)
    
    return number_of_words

def stats(num_list):
    print("total number of reviews: ")
    print(len(num_list))
    print("average review word count: ")
    print(statistics.mean(num_list))
    print("the most common length of reviews: ")
    print(statistics.mode(num_list))

    print("the longest review is: ")
    print(max(num_list))
 

neg_directory = 'aclImdb/test/neg/'
pos_directory = 'aclImdb/test/pos/'

extra_stops = ['br', 'us', 'mr', 'saw', 'until', 'no', 'when', 'with', 
            'like', 'just', 'even', 'it\'s', 'i\'m', 
            'who', 'i\'ve', 'what', 'he', 'see', 'up','get', 'been',
            'because', 'into', 'time', 'watch', 'â–','called', '2',
             '10', 'said','their', 'can','two', 'go', 'also', 'seen', 'him',
            'through', 'it', 'doesn\'t', 'you\'re', 'that\'s', 'there\'s',
            'come', 'said', 'all.', 'screen', 'person', 'i\'ll', 'is,'
            '5', 'sandra', 'them.', '3', '.', 'he\'s', 'man', 'they\'re',
            '\\\x96', '--', 'i\'d', 'is,', 'oh', 'one', 'much', 'movies',
            'say', '4', '1', 'five', 'what\'s', '15', 'ed', '...',
            'movie', 'film','', '-', 'people', 'could', 'make', 'films', 'reviews']


stop_words = nltk.corpus.stopwords.words("english")
stop_list = set(stop_words)
stop_list.update(extra_stops) 
n = 15
combined = []
words_final = []
# review_lengths = []
# iterate thru filenames in a specified folder
for filename in os.listdir(pos_directory)[:n]:
    
    fname = os.path.join(pos_directory, filename)
    # checking if it is a file and opening it
    if os.path.isfile(fname):
        #counting file
        # review_lengths.append(wordCount(fname))
        with open(fname, encoding="utf8") as f:
            raw_words = (f.read().split())
            for word in raw_words: combined.append(word)
            # cleaning the words
            no_punc_words = list(map(remove_punc, combined))
            tagged_words = nltk.tag.pos_tag(no_punc_words, tagset='universal')
            clean_tagged_words = [word for word,tag in tagged_words if tag == 'ADJ' or tag == 'ADV' or tag == 'VERB']
            # putting them into list
            limbo = list(map(make_lower, clean_tagged_words))

[words_final.append(word) for word in limbo if word not in stop_list]
word_counter = Counter(words_final)

# print(no_punc_words)
print(len(tagged_words))
print(len(limbo))
print(len(word_counter))
for word in word_counter.most_common(200):
    print(word)

