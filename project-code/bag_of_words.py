import sys
from functions import *
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer
import numpy as np
import pandas as pd
import nltk
from multiprocessing.resource_sharer import stop
import os
import statistics
from collections import Counter
from tkinter.tix import DisplayStyle

neg_directory = 'aclImdb/test/neg/'
pos_directory = 'aclImdb/test/pos/'

# number of documents to read
n = 5
reviews_final = []
# review_lengths = []
# iterate thru filenames in a specified folder
for filename in os.listdir(pos_directory)[:n]:
    fname = os.path.join(pos_directory, filename)
    # checking if it is a file and opening it
    if os.path.isfile(fname):
        # counting file
        # review_lengths.append(wordCount(fname))
        with open(fname, encoding="utf8") as f:
            # print(filename)
            raw_words = f.read().split()
            no_punc_words = list(map(remove_punc, raw_words))
            no_br_words = list(map(remove_BR, no_punc_words))
            words_no_num = remove_numbers(no_br_words)
            tagged_words = nltk.tag.pos_tag(words_no_num, tagset='universal')
            clean_tagged_words = [word for word, tag in tagged_words if (
                tag == 'ADJ' or tag == 'ADV' or tag == 'VERB')]
            words_lower = list(map(make_lower, words_no_num))

            short_review = ' '.join(remove_words(words_lower))

            reviews_final.append(short_review)

# print(reviews_final)
count = CountVectorizer()
word_count = count.fit_transform(reviews_final)
# print(word_count)
# print(word_count.shape) # how to read -> (x,y) where x is the number of documents being looked at and y is the unique words

tfidf_transformer = TfidfTransformer(smooth_idf=True, use_idf=True)
tfidf_transformer.fit(word_count)
df_idf = pd.DataFrame(tfidf_transformer.idf_,
                      index=count.get_feature_names_out(), columns=["idf_weights"])

# inverse document frequency
df_idf.sort_values(by=['idf_weights'])


# tfidf
tf_idf_vector = tfidf_transformer.transform(word_count)
feature_names = count.get_feature_names_out()

first_document_vector = tf_idf_vector[1]
df_tfifd = pd.DataFrame(first_document_vector.T.todense(),
                        index=feature_names, columns=["tfidf"])
df_sorted = df_tfifd.sort_values(by=["tfidf"], ascending=False)
print(df_sorted.to_string())


# original_stdout = sys.stdout # Save a reference to the original standard output

# with open('filename.txt', 'w') as f:
#     sys.stdout = f # Change the standard output to the file we created.
#     print()
#     sys.stdout = original_stdout
