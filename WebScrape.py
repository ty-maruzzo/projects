from bs4 import BeautifulSoup
import requests
import re

olympian_gods =["Zeus", "Hera", "Poseidon", "Demeter", "Athena", "Apollon",
    "Artemis", "Ares", "Hephaistos", "Aphrodite", "Hermes",
     "Dionysos"]
data = []
headers = {"user-agent": "Chrome 147 on macOS (Monterey)"}


for i in olympian_gods:
    url = 'https://www.theoi.com/Olympios/' + str(i) + ".html"
    with requests.get(url,headers = headers) as f:
        soup = BeautifulSoup(f.text,"lxml")
        
        print(f'Information of {i} is shown here: ')
        myth_tag = soup.find(['h2', 'h3'], string=["MYTHS", "HERMES MYTHS"])
        if myth_tag:
            myth = myth_tag.find_next('p')
            not_myth = myth.find(string = re.compile("famous myths"))
            if not_myth:
                myth = myth.find_next('p')
            myth = re.sub(r'\<\<.*\>\>', '', myth.text)
            print(f' Myths of the God include : {myth.strip()}')

        print("\n \n \n")
        family_tag = soup.find('h2', id = 'Family')
        if family_tag:
            if i == "Aphrodite":
                print("She was born of a sea foam")
                continue
            family = family_tag.find_next('p')
            family = re.sub(r'\[.*\]','',family.text)
            family = re.sub(r'\(.*,','', family)
            parents =" ".join(family.split()[:4])
            print(f'Parents of {i} were {parents}' if family else 'No Family content found')
url = "https://www.theoi.com/Titan/Titanes.html"
with requests.get(url,headers=headers) as d:
    soup = BeautifulSoup(d.text,'lxml')
    find_paragraph = soup.find(src="../image/T20.1Titanes.jpg")
    for i in range(3):
        paragraph = find_paragraph.find_next('p')
        print(paragraph.text.strip())