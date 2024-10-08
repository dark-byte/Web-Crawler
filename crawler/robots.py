import requests
from urllib.parse import urlparse

def can_crawl(url):
    parsed_url = urlparse(url)
    robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"
    try:
        response = requests.get(robots_url)
        if response.status_code == 200:
            rules = response.text
            return check_rules(rules, parsed_url.path)
    except requests.RequestException:
        return True  # Default to True if we can't access robots.txt
    return True

def check_rules(rules, path):
    lines = rules.splitlines()
    user_agent = '*'
    disallowed_paths = []

    for line in lines:
        line = line.strip()
        if line.startswith('User-agent:'):
            user_agent = line.split(':')[1].strip()
        elif line.startswith('Disallow:') and user_agent == '*':
            disallowed_path = line.split(':')[1].strip()
            disallowed_paths.append(disallowed_path)

    return not any(path.startswith(disallowed_path) for disallowed_path in disallowed_paths)

def get_crawl_delay(rules):
    lines = rules.splitlines()
    for line in lines:
        if line.startswith('Crawl-delay:'):
            return int(line.split(':')[1].strip())
    return 1  # Default to 1 second if not specified
