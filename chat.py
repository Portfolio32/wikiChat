from convertHTML import paragraphs, htmlCleaner, indexSelect
from filter import filter
from requester import wikiSearch, getRequest
import requests

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

    url = urls[indexSelect(titles)]
    x = getRequest(url)

    # Convert's HTML to filtered sentences in a list
    clean_text = htmlCleaner(paragraphs(x.text))
    filtered_sentences = filter(clean_text)
    print(filtered_sentences)




    
if __name__ == "__main__":
    main()


