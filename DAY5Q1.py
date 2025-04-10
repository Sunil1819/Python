from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
def fetchlink(url):
    resp=requests.get(url)
    soup=BeautifulSoup(resp.text,'html.parser')
    return [link.get('href') for link in soup.find_all('a',href=True)]
def download_threaded(urls):
    with ThreadPoolExecutor() as e:
        res=e.map(fetchlink,urls)
    return list(res)
url = "https://www.google.com/"
print(fetchlink(url))