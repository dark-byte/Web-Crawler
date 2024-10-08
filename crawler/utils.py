import requests
from bs4 import BeautifulSoup
import urllib.parse

def estimate_links(url, depth=2, headers=None):
    """Estimate the number of links on a website."""
    estimated_links = 0
    if depth == 0:
        return estimated_links
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', href=True)
            estimated_links += len(links)

            for link in links:
                href = link['href']
                absolute_url = urllib.parse.urljoin(url, href)
                estimated_links += estimate_links(absolute_url, depth - 1, headers)

    except requests.RequestException:
        pass

    return estimated_links
