import requests

from loader import config


def testest(start_date, end_date):
    resp = requests.get(f"http://localhost:8000/period/stocks/{start_date}/{end_date}",
                        headers={"access_token": config.misc.api_key})
    return resp.text


if __name__ == "__main__":
    var = testest('2021-06-05', '2021-06-05')
    print(var)
