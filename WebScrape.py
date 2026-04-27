from bs4 import BeautifulSoup
import requests


search =["Zeus", "Hera", "Poseidon", "Demeter", "Athena", "Apollon",
    "Artemis", "Ares", "Hephaistos", "Aphrodite", "Hermes",
     "Dionysos"]
data = []
headers = {"user-agent": "Chrome 147 on macOS (Monterey)"}



for i in search:
    url = 'https://www.theoi.com/Olympios/' + str(i) + ".html"
    with requests.get(url,headers = headers) as f:
        soup = BeautifulSoup(f.text,"lxml") 
        print(url)
        print(f.status_code)
        paras = [a.text.strip() for a in soup.find_all('p')]
        data.append(paras)
        ency_tag = soup.find(id='Encyclopedia')
        if ency_tag:
            ency = ency_tag.find_next('p')
        else:
            print("No Encyclopedia id found")
print(ency.strip())
       