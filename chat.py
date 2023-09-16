from strainer import paragraphs, htmlCleaner, indexSelect
from language import filter_text, filter_sentence, text_to_sentences, matches
from requester import wikiSearch, getRequest

def options(titles: list) -> None:
    """ Print's out the list of title's"""
    for title in titles:
        print(title)

def top_match(question:str, filtered_sentences:list)->int:
    """ Return the greatest number of matches as an int"""
    greatest_number_of_matches = 0
    for filtered_sentence in filtered_sentences:
        number_of_matches = matches(question, filtered_sentence)
        if number_of_matches > greatest_number_of_matches:
            greatest_number_of_matches = number_of_matches
    return greatest_number_of_matches

def top_indexs(question:str, filtered_sentences:list, greatest_number_of_matches) -> set:
    """ Return's a set with the index of top matches"""
    indexs = set()
    for filtered_sentence in filtered_sentences:
        if matches(question, filtered_sentence) == greatest_number_of_matches:
            indexs.add(filtered_sentences.index(filtered_sentence))
    return indexs

def answers(indices:set,sentences:list)-> None:
    """ Prints out the answers"""
    for i in indices:
       print(sentences[i])

def main():
    #Perform wikiSearch and store's top 5 titles and urls and prints the titles
    search = input("What do you want to know about? ")
    DATA = wikiSearch(search)
    titles = DATA[1]
    urls = DATA[3]
    options(titles)
    
    #Select's the correct url in the from the title, and requests data
    url = urls[indexSelect(titles)]
    x = getRequest(url)

    # Convert's HTML to filtered sentences in a list
    clean_text = htmlCleaner(paragraphs(x.text))
    sentences = text_to_sentences(clean_text)
    filtered_sentences = filter_text(clean_text)
    
    #Prints out description
    print(sentences[0])

    #Asks the user for a question
    question = filter_sentence(input("What is your question? "))
    
    #Finds the top matches, stores thoses sentences indices into top_index
    greatest_number_of_matches = top_match(question, filtered_sentences)
    top_index = top_indexs(question, filtered_sentences,greatest_number_of_matches)
    
    #Prints out the top answers based on greatest number of matches
    answers(top_index, sentences)
    
if __name__ == "__main__":
    main()


