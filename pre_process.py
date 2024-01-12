import numpy as np
import nltk
#nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
import gensim
from gensim.models import Word2Vec,KeyedVectors

def tokenize(sentence):
    
    return nltk.word_tokenize(sentence)


def stem(word):
    return stemmer.stem(word.lower())



from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize  # You may need to install the nltk library: pip install nltk

def get_word_vectors(sentences, vector_size=100, window=5, min_count=1, workers=4):
    """
    Get word vectors from a list of sentences.

    Parameters:
    - sentences: List of sentences (each sentence is a string).
    - vector_size: Dimensionality of the word vectors.
    - window: Maximum distance between the current and predicted word within a sentence.
    - min_count: Ignores all words with a total frequency lower than this.
    - workers: Number of CPU cores to use for training.

    Returns:
    - List of lists, where each inner list represents the word vectors for a sentence.
    """
    # Tokenize the sentences into words
    tokenized_sentences = [word_tokenize(sentence.lower()) for sentence in sentences]

    # Train the Word2Vec model
    model = Word2Vec(sentences=tokenized_sentences, vector_size=vector_size, window=window, min_count=min_count, workers=workers)

    # Get word vectors for each sentence
    word_vectors = [model.wv[words] for words in tokenized_sentences]

    return word_vectors

# Example usage
sentences = [
    "This is an example sentence.",
    "Word embeddings are interesting.",
    "Gensim makes it easy to work with word vectors."
]

word_vectors = get_word_vectors(sentences)

# Display word vectors for each sentence
'''
for i, vectors in enumerate(word_vectors):
    print(f"Sentence {i + 1} word vectors: {vectors}")
'''
# comment one you can convert when you are needed

