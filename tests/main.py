import requests

from data.config import API_KEY


def testest():
    resp = requests.get("http://localhost:8000/today/stocks",
                        headers={"access_token": API_KEY})
    return resp.text


if __name__ == "__main__":
    var = testest()
    print(var)
