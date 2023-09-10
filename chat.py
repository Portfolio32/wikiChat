from convertHTML import paragraphs, htmlCleaner
from filter import filter
import requests
import re



def main():
    # I need to work on automating the search by user input by using API's
    S = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php"
    #user input here for what they want to search about
    search = input("What do you want to know about? ")
    PARAMS = {
        "action": "opensearch",
        "namespace": "0",
        "search": f"{search}",
        "limit": "5",
        "format": "json"
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    print(type(DATA))
    titles = DATA[1]
    for title in titles:
        print(title)
    
    user_input = input("Which one specifically? ")
    user_input = user_input.replace("(", "").replace(")", "")
    index = 0
    for title in titles:
        if re.fullmatch(f"{title.replace('(', '').replace(')', '')}", user_input, re.IGNORECASE):
            index = titles.index(title)
    url = DATA[3][index]
    x = requests.get(url)


    # Convert's HTML to filtered sentences in a list
    clean_text = htmlCleaner(paragraphs(x.text))
    filtered_sentences = filter(clean_text)
    #print(filtered_sentences)

    # Next part would be matching with user defined question's with the sentences
    # should start off by asking what they want to search for
    # Question filtering

    
if __name__ == "__main__":
    main()


