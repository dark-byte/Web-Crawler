import requests
from bs4 import BeautifulSoup
import urllib.parse
import sys
import time
import threading
from .robots import can_crawl, get_crawl_delay
from tqdm import tqdm
from .utils import estimate_links

class WebScraper:
    def __init__(self, domain, keyword):
        self.domain = domain
        self.keyword = keyword
        self.visited = set()
        self.results = []
        self.headers = {
            'User-Agent': 'SearchCrawler/1.0 (https://github.com/dark-byte/Web-Crawler)'
        }
    
    def spinner_animation(self):
        """Display a spinner animation."""
        spinner = ['-', '\\', '|', '/']
        while not self.stop_spinner.is_set():
            for frame in spinner:
                sys.stdout.write(f'\r{frame} Estimating Number of Links...')
                sys.stdout.flush()
                time.sleep(0.1)

    def crawl(self):
        self.stop_spinner = threading.Event()
        spinner_thread = threading.Thread(target=self.spinner_animation)

        # Start the spinner thread
        spinner_thread.start()

        total_links = estimate_links(self.domain, depth=2)  # Estimate total links

        self.stop_spinner.set()  # Stop the spinner
        spinner_thread.join()  # Wait for the spinner thread to finish

        with tqdm(total=total_links, desc="Crawling", unit="link") as pbar:
            self.get_links(self.domain, pbar)

        return self.results

    def get_links(self, url, pbar):
        if url in self.visited:
            return
        self.visited.add(url)

        if not can_crawl(url):
            print(f"Blocked by robots.txt: {url}")
            return

        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code != 200:
                return
            soup = BeautifulSoup(response.text, 'html.parser')

            for link in soup.find_all('a', href=True):
                href = link['href']
                absolute_url = urllib.parse.urljoin(url, href)

                if self.domain in absolute_url and absolute_url not in self.visited:
                    if self.keyword.lower() in link.get_text().lower():
                        self.results.append(absolute_url)

                    # Recursive call
                    self.get_links(absolute_url, pbar)

                    # Update progress bar after each link
                    pbar.update(1)

            # Respect Crawl-delay after processing links
            delay = get_crawl_delay(requests.get(f"{self.domain}/robots.txt").text)
            time.sleep(delay/2)

        except requests.RequestException as e:
            print(f"Error accessing {url}: {e}")