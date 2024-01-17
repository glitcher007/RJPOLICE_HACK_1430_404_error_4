import numpy as np
import nltk
#nltk.download('punkt')
import spacy
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
#nltk.download('stopwords')
import nltk
from nltk.corpus import stopwords
import string
from nltk.tokenize import word_tokenize



#nltk.download('stopwords')
#nltk.download('punkt')
stemmer = PorterStemmer()


def tokenize(sentence):
    
    return nltk.word_tokenize(sentence)


def stem(text):
    stemmer = PorterStemmer()

    # Tokenize the text into words
    words = word_tokenize(text)

    # Apply stemming to each word
    stemmed_words = [stemmer.stem(word) for word in words]

    # Reconstruct the text with stemmed words
    result_text = ' '.join(stemmed_words)

    return result_text



def perform_ner(text):
    # Load spaCy English language model
    nlp = spacy.load("en_core_web_sm")

    # Process the text with spaCy NLP pipeline
    doc = nlp(text)

    # Extract named entities
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    return entities

def Lower(text):
    return text.lower()

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))

    # Tokenize the text into words
    words = word_tokenize(text)

    # Remove stopwords
    filtered_words = [word for word in words if word.lower() not in stop_words]

    # Reconstruct the text without stopwords
    result_text = ' '.join(filtered_words)

    return result_text

def remove_specific_characters(text):
    # Define the set of characters to be removed
    chars_to_remove = set(['.', ',', '[', ']', '(', ')', '{', '}', '/', '\\',':','-','>','<','?','  '])

    # Remove specified characters from the text
    cleaned_text = ''.join(char for char in text if char not in chars_to_remove)

    return cleaned_text

def remove_punctuations(text):
    # Define the set of punctuation characters
    punctuation_chars = set(string.punctuation)

    # Remove punctuation characters from the text
    cleaned_text = ''.join(char for char in text if char not in punctuation_chars)

    return cleaned_text



 





def bag_of_words(tokenized_sentence, words):
   
    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag