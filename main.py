from application.generator import text_read
import json
from application.downloader import downloader
from application.links import *


with open(f"db/{'countries.json'}", 'wb') as file:
    for chunk in downloader(netology_link, 16):
        file.write(chunk)

with open("db/countries.json", encoding='utf-8') as f:
    data = json.load(f)
    countries_links = {}

    for part in data:
        countries = part['name']['common']
        countries = countries.replace(' ', '_')
        countries_links[countries] = (wiki_link + countries)
        with open(f"db/{'all_countries.txt'}", 'a', encoding='utf-8') as f1:
            f1.write(countries + '\n')

    for x, y in countries_links.items():
        with open(f"db/{'all_links.txt'}", 'a', encoding='utf-8') as result:
            result.write(x + ' : ' + y + '\n')


def main():
    output = text_read('db/all_links.txt')
    for i in output:
        print(i)


if __name__ == '__main__':
    main()

