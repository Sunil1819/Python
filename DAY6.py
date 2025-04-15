import requests
import asyncio
import aiohttp
from bs4 import BeautifulSoup
def make_absolute(base,link):
    if link.startswith("http"):
        return link
    elif link.startswith("/"):
        return base.rstrip("/") + link
    else:
        return base.rstrip("/") + "/" + link
def get_initial_links(base_url):
    print(f"Downloading main page: {base_url}")
    response = requests.get(base_url)
    if response.status_code != 200:
        print(f"Failed to fetch {base_url}: Status {response.status_code}")
        return []
    soup = BeautifulSoup(response.text, 'html.parser')
    raw_links = [tag['href'] for tag in soup.find_all('a',href=True)]
    absolute_links = [make_absolute(base_url, link) for link in raw_links]
    return absolute_links
async def fetch_link(session,url):
    async with session.get(url) as resp:
        if resp.status != 200:
            print(f"Failed to download {url}: Status {resp.status}")
            return None
        print(f"Downloaded: {url}")
        return await resp.text()
async def download_all_links(links):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_link(session, link) for link in links]
        return await asyncio.gather(*tasks)
def main():
    base_url = "https://www.google.com"
    links = get_initial_links(base_url)
    if links:
        print(f"Found {len(links)} links. Downloading...")
        asyncio.run(download_all_links(links))
    else:
        print("No links found.")
if __name__ == "__main__":
    main()
