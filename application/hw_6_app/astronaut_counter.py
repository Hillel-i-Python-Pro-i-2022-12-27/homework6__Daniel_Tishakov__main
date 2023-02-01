import requests


def austronaut_counter():
    response = requests.get("http://api.open-notify.org/astros.json")
    data = response.json()
    result = []
    for i in data["people"]:
        result.append(i["name"])
    return result


if __name__ == "__main__":
    austronaut_counter()
