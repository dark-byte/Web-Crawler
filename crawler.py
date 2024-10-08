import json
from crawler.scraper import WebScraper
from datetime import datetime
import os

def main():
    domain = input("Enter the domain to crawl (e.g., https://example.com): ")
    keyword = input("Enter the search keyword: ")

    scraper = WebScraper(domain, keyword)
    found_links = scraper.crawl()

    # Create directory if it doesn't exist
    output_dir = 'results'
    os.makedirs(output_dir, exist_ok=True)

    # Generate a unique filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{output_dir}/{keyword}_{timestamp}.json"

    # Exporting results to JSON
    with open(filename, 'w') as json_file:
        json.dump(found_links, json_file, indent=4)

    print(f"Found {len(found_links)} links mentioning '{keyword}'. Results exported to {filename}.")

if __name__ == "__main__":
    main()
