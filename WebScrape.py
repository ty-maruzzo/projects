from bs4 import BeautifulSoup
import requests
import re

god =["Zeus", "Hera", "Poseidon", "Demeter", "Athena", "Apollon",
    "Artemis", "Ares", "Hephaistos", "Aphrodite", "Hermes",
     "Dionysos"]
data = []
headers = {"user-agent": "Chrome 147 on macOS (Monterey)"}


for i in god:
    url = 'https://www.theoi.com/Olympios/' + str(i) + ".html"
    with requests.get(url,headers = headers) as f:
        soup = BeautifulSoup(f.text,"lxml")
        
        print(f'Information of {i} is shown here: ')
        ency_tag = soup.find(id='Encyclopedia')
        if ency_tag:
            ency = ency_tag.find_next('p')
            #print(ency)
        else:
            print("No Encyclopedia id found")
        passage_ency =" ".join(ency.text.split()[:27])
        print(passage_ency)
        myth_tag = soup.find(['h2', 'h3'], string=["MYTHS", "HERMES MYTHS"])
        if myth_tag:
            myth = myth_tag.find_next('p')
            not_myth = myth.find(text = re.compile("famous myths"))
            if not_myth:
                myth = myth.find_next('p')
            passage_myth = " ".join(myth.text.split()[:27])
            print(f' Myths of the God include : {passage_myth}')
        family_tag = soup.find('h2', id = 'Family')
        if family_tag:
            if i == "Aphrodite":
                print("She was born of a sea foam")
                continue
            family = family_tag.find_next('p')
            parents =" ".join(family.text.split()[:4])
            print(f'Parents of {i} were {parents}' if family else 'No Family content found')
        
        