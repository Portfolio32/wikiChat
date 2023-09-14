from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

def text_to_sentences(text: str)-> list:
    """ Tokenizes the text into sentences"""
    return sent_tokenize(text)

def filter_text(text: str) -> list:
    """
    Takes in text and return's a list of filtered sentences
    Parses out stop-words and lemmatizes each word

    """
    filtered_sentences = []
    lem = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))
    sentences = sent_tokenize(text)
    for sentence in sentences:
        words = word_tokenize(sentence)
        new_sentence = [lem.lemmatize(word) for word in words if word not in stop_words]
        filtered_sentence = TreebankWordDetokenizer().detokenize(new_sentence)
        filtered_sentences.append(filtered_sentence)
    return filtered_sentences


def filter_sentence(sentence:str)-> str:
    """Takes in sentence and return's the filtered version"""
    lem = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(sentence)
    new_sentence = [lem.lemmatize(word) for word in words if word not in stop_words]
    return TreebankWordDetokenizer().detokenize(new_sentence)

def synonyms(word: str)-> list:
    """Take a word and return's a set of synonyms """
    synonyms = set()
    for syn in wordnet.synsets(f"{word}"):
        for name in syn.lemma_names():
            synonyms.add(name)
    return synonyms