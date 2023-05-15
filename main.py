import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Style

# Initialize colorama
init()

# Define color codes
SUCCESS_COLOR = Fore.GREEN
FAILURE_COLOR = Fore.RED
RESET_COLOR = Style.RESET_ALL

def check_sitemap(sitemap_url):
    response = requests.get(sitemap_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'xml')
        urls = soup.find_all('loc')
        url_list = [url.text for url in urls]
        return url_list
    else:
        print(f"{FAILURE_COLOR}Error accessing sitemap.{RESET_COLOR}")
        return []

def check_robots(robots_url):
    response = requests.get(robots_url)
    if response.status_code == 200:
        disallowed_urls = []
        for line in response.text.split('\n'):
            if line.startswith('Disallow:'):
                disallowed_url = line.split(': ')[1].strip()
                disallowed_urls.append(disallowed_url)
        return disallowed_urls
    else:
        print(f"{FAILURE_COLOR}Error accessing robots.txt.{RESET_COLOR}")
        return []

def check_disallowed(disallowed_urls):
    for url in disallowed_urls:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{SUCCESS_COLOR}[+] Access to {url} successful (200 OK).{RESET_COLOR}")
        else:
            print(f"{FAILURE_COLOR}[-] Access to {url} failed.{RESET_COLOR}")

# Example usage:
sitemap_url = 'https://www.example.com/sitemap.xml'
robots_url = 'https://www.example.com/robots.txt'

sitemap_content = check_sitemap(sitemap_url)
print(f"{Style.BRIGHT}Sitemap URLs:")
for url in sitemap_content:
    print(url)

print("\n")

robots_content = check_robots(robots_url)
print(f"{Style.BRIGHT}Disallowed URLs:")
for url in robots_content:
    print(url)

print("\n")

print(f"{Style.BRIGHT}Checking disallowed URLs:")
check_disallowed(robots_content)
