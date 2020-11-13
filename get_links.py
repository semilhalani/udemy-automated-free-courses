from selenium.webdriver.remote.webdriver import WebDriver

from core import TutorialBarScraper

import requests
from bs4 import BeautifulSoup

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }


links = []
tb_scraper = TutorialBarScraper()

print('1. IT software')
print('2. Development')
print('3. Finance Accounting')
print('4. Design')
print('5. Business')
print('6. Marketing')
print('7. Health and Fitness')
print('8. Office Productivity')
print('9. Photography')
print('10. Personal Development')
print('11. Teaching and Academics')
print('99. All Courses')
choice = input('Please select what category you want? :')
count = 1
while True:
    udemy_course_links = tb_scraper.run(choice)
    for course_link in udemy_course_links:
        url = course_link
        req = requests.get(url, headers)
        soup = BeautifulSoup(req.content, 'html.parser')
        url_body = soup.get_text()
        """url_formatted_body = url_body.split("\n",5)
        title = url_formatted_body[4]
        if '|' in title:
            updated_title = title.split("|")
            print(str(count) + ". " + updated_title[0])
        else:
            print(str(count) + ". " + title)"""
        headline_tag = soup.find("div", { "class" : "udlite-text-md clp-lead__headline" })
        print(str(count) + ". " + headline_tag.text.strip())
        print(url)
        print()
        count = count + 1

print(links)
print(len(links))
