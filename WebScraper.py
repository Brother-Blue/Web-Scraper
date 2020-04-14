import requests
import pandas as p
import os.path

from bs4 import BeautifulSoup

url = "https://www.monster.se/jobb/sok/?q=software-engineer&where=gothenburg&cy=se&intcid=swoop_HeroSearch_SE"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='SearchResults')
job_els = results.find_all('section', class_='card-content')

titles = []
companies = []
locations = []

for job in job_els:
    title = job.find('h2', class_='title')
    company = job.find('div', class_='company')
    location = job.find('div', class_='location')
    if None in (title, company, location):
        continue
    titles.append(title.text.strip())
    companies.append(company.text.strip())
    locations.append(location.text.strip())
    print(title.text, company.text, location.text)
    print()

frame = p.DataFrame({'Job Title': titles, 'Company': companies, 'Location': locations})

save_to_path = "~/Desktop"
file_name = input("Save file as: ")
save_file_name = os.path.join(save_to_path, file_name + ".csv")
frame.to_csv(save_file_name, index=False, encoding="utf-8")