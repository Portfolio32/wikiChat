from convertHTML import paragraphs, htmlCleaner, indexSelect
from filter import filter_text, filter_sentence, text_to_sentences
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
    print(len(sentences))
    print(len(filtered_sentences))
    #filter question
    #while True:
    #question = filter_sentence(input("What is your question? "))




    


    
if __name__ == "__main__":
    main()


