import nltk
import statistics

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