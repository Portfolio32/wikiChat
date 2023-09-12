from bs4 import BeautifulSoup, SoupStrainer
import re

def paragraphs(html_doc: str) -> str:
    """ Gets the paragraph tags out of the html file"""
    strain = SoupStrainer("p")        
    return BeautifulSoup(html_doc, "html.parser", parse_only=strain).get_text()

def htmlCleaner(html: str) -> str:
    """ Deletes bracket citations and html tags"""
    text = re.sub(r"<.*?>"," " ,html , flags=re.IGNORECASE)
    text = text.strip()
    return re.sub(r"\[\d+\]", " ", text)
    
def indexSelect(titles: list) -> int:
    user_input = input("Which one specifically? ").replace("(", "").replace(")", "")
    for title in titles:
        if re.fullmatch(f"{title.replace('(', '').replace(')', '')}", user_input, re.IGNORECASE):
            index = titles.index(title)
    return index