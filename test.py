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
matching = word_tokenize(matching)
sentence = word_tokenize(sentence)
# I'm thinkiing this might be an issue if for example we have words
# that are going to be doubled and that would happen if i use synonyms
matched = []
#I guess we can append used words already
for m in matching:
    # what is wrong here?
    if m in sentence and m not in matched:
        matches += 1
        matched.append(m)
        
        
print(matches)