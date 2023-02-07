import requests

from data.config import API_KEY


def testest(start_date, end_date):
    resp = requests.get(f"http://localhost:8000/period/stocks/{start_date}/{end_date}",
                        headers={"access_token": API_KEY})
    return resp.text


if __name__ == "__main__":
    var = testest('2021-06-05', '2021-06-05')
    print(var)
