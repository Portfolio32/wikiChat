from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk.stem import WordNetLemmatizer


def filter(text: str) -> list:
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