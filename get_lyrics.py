import requests


def get_lyrics(filename) -> str:
    url = "https://lrclib.net/api/search"
    params = {"q": filename}
    response = requests.get(url, params=params)

    if response.status_code == 200 and response.json():
        results = response.json()
        return results[0].get("plainLyrics")
    else:
        return "No Lyrics Found"


# print(get_lyrics("Blacklite - Cold As Ice"))
