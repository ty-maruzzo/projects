from bs4 import BeautifulSoup
import requests


search =["Zeus", "Hera", "Poseidon", "Demeter", "Athena", "Apollo",
    "Artemis", "Ares", "Hephaestus", "Aphrodite", "Hermes",
    "Hestia", "Dionysus", "Hades"]
data = []
headers = {"user-agent": "Chrome 147 on macOS (Monterey)"}



for i in search:
    url = 'https://en.wikipedia.org/wiki/' + str(i)
    with requests.get(url,timeout=5,headers = headers) as f:
        soup = BeautifulSoup(f.text,"lxml") 
        print(url)
        print(f.status_code)
        paras = [a.text for a in soup.find_all('p')]
        data.append(paras)



