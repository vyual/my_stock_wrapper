import requests

from data.config import API_KEY


def testest():
    resp = requests.get("http://localhost:8000/wholesale/2021-08-11/2021-09-12/39c6669a-bd75-11e8-9107-50480002c54a",
                        headers={"access_token": API_KEY})
    print(resp.text)


if __name__ == "__main__":
    testest()
