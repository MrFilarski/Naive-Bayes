import codecs
import csv
import urllib.request


def get_from_path(path) -> list[list[str]]:
    try:
        with open(path) as file:
            return [row for row in csv.reader(codecs.iterdecode(file, 'utf-8'))]
    except FileNotFoundError:
        print(f"file {path} not found")


def get_from_url(destination: str) -> list[list[str]]:
    url = "https://users.pja.edu.pl/~shorawa/nai2022pl/" + destination
    response = urllib.request.urlopen(url)
    return [text.decode("UTF-8") for text in response.readlines()]
