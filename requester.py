import requests


def wikiSearch(search: str)-> list:
    """Wikipedia Opensearch API"""
    S = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
        "action": "opensearch",
        "namespace": "0",
        "search": f"{search}",
        "limit": "5",
        "format": "json"
    }
    R = S.get(url=URL, params=PARAMS)
    return R.json()


