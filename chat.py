from strainer import paragraphs, htmlCleaner, indexSelect
from language import filter_text, filter_sentence, text_to_sentences
from requester import wikiSearch, getRequest

def options(titles: list) -> None:
    """ Print's out the list of title's"""
    for title in titles:
        print(title)

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
    print(filtered_sentences)

    
    greatest_number_of_matches = 0

    question = filter_sentence(input("What is your question? "))
    # I should check matches for each sentence in the text
    # for each sentence track the number of matches
    
    # have a variable that sotres the greates number of matches
    # if that sentence has the greatest number of matches
    # store the index of that sentence as the most close
    
    

    


    


    
if __name__ == "__main__":
    main()


