from selenium import webdriver
from bs4 import BeautifulSoup
from chrome_options import chrome_options
from extractURLs import extractURL
import json
import urllib3

f = open('config.json',)
config = json.load(f)
primary_url = config['url']
f.close();

driver = webdriver.Chrome('chromedriver', options=chrome_options)
driver.get(primary_url)


p_element = driver.page_source
driver.quit();

soup = BeautifulSoup(p_element, 'html.parser')
links = [a['href'] for a in soup.select('a[href]')]

extract = extractURL(primary_url,links)
url_list = extract.extract_main_list()
# print(url_list)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
print(extract.verify_status_code(url_list))

