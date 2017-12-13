import requests


def get_location_info():
    return requests.get("http://freegeoip.net/json/").json()


if __name__ == "__main__":
    obj = get_location_info()
    print(obj.keys())
    print(obj['ip'])
    print(obj['city'])
