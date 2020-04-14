import requests
import pandas as p
import os.path
import tkinter
from bs4 import BeautifulSoup


monster_title = []
monster_company = []
monster_location = []


def monster_search(description, location):
    url = "https://www.monster.com/"
    loc = location.replace(' ', '-')
    page = requests.get(url + description + '&where=' + loc)
    content = BeautifulSoup(page.content, 'html.parser')
    res = content.find(id='SearchResults')
    elements = res.find_all('section', class_='card-content')

    for el in elements:
        t = el.find('h2', class_='title')
        c = el.find('div', class_='company')
        l = el.find('div', class_='location')
        if None in (t, c, l):
            continue
        monster_title.append(t.text.strip())
        monster_company.append(c.text.strip())
        monster_location.append(l.text.strip())

    return None


def search(description):
    # Search on all given websites using description parameter
    return None


root = tkinter.Tk()
root.title("Job hunter")
tkinter.Label(root, text="Enter job description").grid(row=0)
search_entry = tkinter.Entry(root)
search_entry.grid(row=0, column=1)
tkinter.Button(root, text="Exit", command=root.quit()).grid(row=5, column=0, sticky=tkinter.W, pady=5)
tkinter.Button(root, text="Search", command=search(search_entry.get()), row=1, column=1, sticky=tkinter.W, pady=5)

root.mainloop()

'''
dframe = p.DataFrame({'Job Title': titles, 'Company': companies, 'Location': locations})

save_to_path = "~/Desktop"
file_name = input("Save file as: ")
save_file_name = os.path.join(save_to_path, file_name + ".csv")
dframe.to_csv(save_file_name, index=False, encoding="utf-8")
'''
