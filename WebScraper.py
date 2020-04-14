import requests
import pandas as p
import os.path
from bs4 import BeautifulSoup


def monster_search(desc, loc):
    monster_title = []
    monster_company = []
    monster_location = []
    url = "https://www.monster.com/"
    loc = loc.replace(' ', '-')
    page = requests.get(url + 'jobs/search/?q=' + desc + '&where=' + loc)
    content = BeautifulSoup(page.content, 'html.parser')
    res = content.find(id='SearchResults')
    elements = res.find_all('section', class_='card-content')

    for el in elements:
        title = el.find('h2', class_='title')
        company = el.find('div', class_='company')
        location = el.find('div', class_='location')
        if None in (title, company, location):
            continue
        monster_title.append(title.text.strip())
        monster_company.append(company.text.strip())
        monster_location.append(location.text.strip())
    return 'Monster', monster_title, monster_company, monster_location


def search(description='engineer', location='New York City'):
    return monster_search(description, location)


def save_file(s_name="", s_title="", s_company="", s_location=""):
    d_frame = p.DataFrame({'JOB SITE': s_name, 'JOB TITLE': s_title, 'COMPANY': s_company, 'LOCATION': s_location})

    save_to_path = "~/Desktop"
    file_name = input("Save file as: ")
    save_file_name = os.path.join(save_to_path, file_name + ".csv")
    d_frame.to_csv(save_file_name, index=False, encoding="utf-8")
