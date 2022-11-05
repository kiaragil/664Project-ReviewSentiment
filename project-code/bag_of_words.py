from multiprocessing.resource_sharer import stop
import os
import statistics
from collections import Counter
import nltk
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer

def remove_punc(word):
    punc = '''-!()[]{};:"\,<>./?@#$%^&*_~'''
    no_punc_word = word.translate(str.maketrans('', '', punc))
    return no_punc_word

def make_lower(word):
    return word.lower()

def remove_numbers(lst):
    no_num_list = [x for x in lst if not any(c.isdigit() for c in x)]
    return no_num_list

def remove_words(lst):
    extra_stops = ['aa', 'ab','br', 'us', 'mr', 'saw', 'until', 'no', 'when', 'with', 
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

    words = [word for word in lst if word not in stop_list]

    return words

def remove_BR(word):
    if word.endswith('br'):
        word = word[:-2]
    return word
  
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

# test_csv = pd.read_csv('IMDB_Dataset.csv') 
df = pd.read_csv('project-code\IMDB_Dataset.csv')
print(df)

# number of documents to read
# n = 1
# reviews_final = []
# # review_lengths = []
# # iterate thru filenames in a specified folder
# for filename in os.listdir(pos_directory)[:n]:
#     fname = os.path.join(pos_directory, filename)
#     # checking if it is a file and opening it
#     if os.path.isfile(fname):
#         #counting file
#         # review_lengths.append(wordCount(fname))
#         with open(fname, encoding="utf8") as f:
#             # print(filename)
#             raw_words = f.read().split()
#             no_punc_words = list(map(remove_punc, raw_words))
#             no_br_words = list(map(remove_BR, no_punc_words))
#             words_no_num = remove_numbers(no_br_words)
#             tagged_words = nltk.tag.pos_tag(words_no_num, tagset='universal')
#             clean_tagged_words = [word for word,tag in tagged_words if (tag == 'ADJ' or tag == 'ADV' or tag == 'VERB')]
#             words_lower = list(map(make_lower, clean_tagged_words))
#             short_review = ' '.join(remove_words(words_lower))
#             reviews_final.append(short_review)

# word_counter = Counter(words_final)

# print(reviews_final)
#

# count = CountVectorizer()
# word_count=count.fit_transform(reviews_final)
# # print(word_count)
# # print(word_count.shape) # how to read -> (x,y) where x is the number of documents being looked at and y is the unique words 

# tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
# tfidf_transformer.fit(word_count)
# df_idf = pd.DataFrame(tfidf_transformer.idf_, index=count.get_feature_names_out(),columns=["idf_weights"])

# #inverse document frequency
# df_idf.sort_values(by=['idf_weights'])


# #tfidf
# tf_idf_vector=tfidf_transformer.transform(word_count)
# feature_names = count.get_feature_names_out()

# first_document_vector=tf_idf_vector[1]
# df_tfifd= pd.DataFrame(first_document_vector.T.todense(), index=feature_names, columns=["tfidf"])

# df_tfifd.sort_values(by=["tfidf"],ascending=False)
# print(df_tfifd)

# import sys

# print('This message will be displayed on the screen.')

# original_stdout = sys.stdout # Save a reference to the original standard output

# with open('filename.txt', 'w') as f:
#     sys.stdout = f # Change the standard output to the file we created.
#     print(reviews_final)
#     sys.stdout = original_stdout
