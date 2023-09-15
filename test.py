from language import synonyms
from nltk.tokenize import word_tokenize
sentence = "I would like to buy some cream"
matching = "I would like to buy some meme some"
# I could count the number fo matches for each sentence and then 
# have a variable that sotres the greates number of matches
# if that sentence has the greatest number of matches
# store the index of that sentence as the most close
#would be a good idea to have each sentence tokenized to words
greatestMatches = 0
matches = 0
sentenceWords = word_tokenize(matching)
questionWords = word_tokenize(sentence)
# I'm thinkiing this might be an issue if for example we have words
# that are going to be doubled and that would happen if i use synonyms

match = []
matches = 0
for questionWord in questionWords:
    # for each word in the question we want to see if there is a match
    for sentenceWord in sentenceWords:
        # sentenceWord is the Word from the text 
        matched = len((synonyms(questionWord).intersection(synonyms(sentenceWord))))
        # if matches >= 1
        if matched >= 1:
            #then should probably append the matched word and add one
            match.append(sentenceWord)
            matches += 1
            break
print(synonyms("."))