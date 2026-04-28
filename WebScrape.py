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
        myth_tag_athena = soup.find('h3', string="MYTHS")
        if myth_tag_athena:
            myth = myth_tag_athena.find_next('p')
            myth2 = myth.find_next('p')
            print(myth2.text)
        myth_tag = soup.find('h2', string ="MYTHS")
        myth_tag_hermes = soup.find('h2', string = 'HERMES MYTHS')
        if myth_tag_hermes:
            myth = myth_tag_hermes.find_next('p')
            print(myth.text)
        if myth_tag:
            myth = myth_tag.find_next('p')
            print(myth.text)
            if myth and "famous myths" in myth.text:
                myth = myth.find_next('p')
                print(myth.text if myth else "No myth content found")
        