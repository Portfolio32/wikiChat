from code_filter import paragraphs, htmlCleaner, indexSelect
from word_filter import filter_text, filter_sentence, text_to_sentences
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



    #filter question
    #while True:
    question = filter_sentence(input("What is your question? "))

    # match the question to a corresponding sentnece in the text
    # remember the text itself is a lsit of sentences
    # Should I use synonyms? 
    # I think I should. 
    


    


    
if __name__ == "__main__":
    main()


