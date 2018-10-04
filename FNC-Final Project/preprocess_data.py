import nltk
from nltk.corpus import stopwords
from string import punctuation
from itertools import chain

english_stemmer = nltk.stem.SnowballStemmer('english')
stopwords = nltk.corpus.stopwords.words('english')
punct = punctuation

def tokenize(texts):
    # Transform each review string as a list of token strings. May take a few seconds
    word_token = [nltk.word_tokenize(text) for text in texts]
    sentence_token = [nltk.sent_tokenize(text) for text in texts]
    
    return word_token,sentence_token

def stem_tokens(tokens, stemmer):
    stemmed = []
    for doc in tokens:
        stemmed.append([stemmer.stem(token) for token in doc])
    return stemmed

def clean_text(tokenized_list,stem=True,exclude_stopword=True):
    tokens = []
    for doc in tokenized_list:
        tokens.append([token.lower() for token in doc if token.lower() not in chain(punct,stopwords)])
    tokens_stemmed = tokens
    if stem:
        tokens_stemmed = stem_tokens(tokens, english_stemmer)
        
    return tokens_stemmed
