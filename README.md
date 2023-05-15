Sitemap and Robots.txt Checker
This is a Python script that checks the sitemap.xml and robots.txt files of a website. It lists the URLs from the sitemap and extracts the disallowed URLs mentioned in the robots.txt file. Additionally, it attempts to access the disallowed URLs and displays whether the access was successful or not.

Requirements
Python 3.x
requests library
BeautifulSoup library
colorama library
Installation
Ensure you have Python 3.x installed on your system. You can download Python from the official Python website: python.org.

Install the required libraries by running the following command in your command prompt or terminal:

Copy code
pip install requests bs4 colorama
Usage
Open the sitemap_checker.py file in a text editor.

Modify the sitemap_url and robots_url variables to the appropriate URLs you want to check.

Open a command prompt or terminal and navigate to the directory where the script is located.

Run the script by executing the following command:

Copy code
python sitemap_checker.py
The script will display the sitemap URLs, the disallowed URLs from the robots.txt file, and the status of accessing the disallowed URLs (success or failure).
Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please create an issue or submit a pull request.