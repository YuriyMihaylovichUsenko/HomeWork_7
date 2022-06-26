from bs4 import BeautifulSoup
from requests import Session
import json


def main():
    url = 'https://www.netflix.com/ua-ru/browse/genre/34399'
    with Session() as session:
        response = session.get(url, timeout=10)

        assert response.status_code == 200, 'Bad response'
        print(response.status_code)

    soup = BeautifulSoup(response.content, 'html.parser')

    # breakpoint()

    all_picture_from_response = soup.select('.nm-collections-title-img')
    picture_only_url = []
    list_of_indexes = []
    for index, element in enumerate(all_picture_from_response):
        if index % 2 == 0 and element['src'][:5] == 'https':
            picture_only_url.append(element['src'])
            list_of_indexes.append(index)

    all_names_from_response = soup.select('.nm-collections-title-name')
    names_respective_pictures_only_url = []
    for index in list_of_indexes:
        names_respective_pictures_only_url.append(all_names_from_response[int(index/2)].text.strip())
            
    # If it mattered, result can be in list format:
    # result_by_list = list(zip(names_respective_pictures_only_url, picture_only_url))

    result_by_dict = {}
    for index, value in enumerate(names_respective_pictures_only_url):
        result_by_dict[value] = picture_only_url[index]

    with open('book_scraper_HW_7.json', 'w') as file:
        json.dump(result_by_dict, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()
