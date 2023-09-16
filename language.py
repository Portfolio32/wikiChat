from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer
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
        # List comprehension that filters out stopwords and lemmatizes each word
        new_sentence = [lem.lemmatize(word) for word in words if word not in stop_words]
        # Detokenizes list of words back into sentence and then appends to list
        filtered_sentence = TreebankWordDetokenizer().detokenize(new_sentence)
        filtered_sentences.append(filtered_sentence)
    return filtered_sentences


def filter_sentence(sentence:str)-> str:
    """Takes in sentence and return's the filtered version"""
    lem = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(sentence)
    # List comprehension to filter out stopwords and lemmatizes each word
    new_sentence = [lem.lemmatize(word) for word in words if word not in stop_words]
    # Return's the list of words converted back into string 
    return TreebankWordDetokenizer().detokenize(new_sentence)

def synonyms(word: str)-> set:
    """Take a word and return's a set of synonyms """
    synonyms = set()
    for syn in wordnet.synsets(f"{word}"):
        for name in syn.lemma_names():
            synonyms.add(name)
    return synonyms

def matches(question:str,textSentence:str)-> int:
    """number of matches for a sentence and question"""
    number_of_matches = 0
    # Word tokenizes that only recognizes word characters and '
    tokenizer = RegexpTokenizer(r"[\w']+")
    sentenceWords = tokenizer.tokenize(textSentence)
    questionWords = tokenizer.tokenize(question)
    # We're matching from the list of question words
    for questionWord in questionWords:
        # Variable to enable double check for synonyms if needed
        double_check = True

        # Check each sentence word for a match
        for sentenceWord in sentenceWords:
            if questionWord == sentenceWord:
                number_of_matches += 1
                double_check = False
                break
        if double_check == True:    
            for sentenceWord in sentenceWords:
                matched = len((synonyms(questionWord).intersection(synonyms(sentenceWord))))
                if matched >= 1 and sentenceWord:
                    number_of_matches += 1
                    break
    return number_of_matches