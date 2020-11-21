from selenium.webdriver.remote.webdriver import WebDriver

from core import TutorialBarScraper

from bs4 import BeautifulSoup

import requests, datetime

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
directory = "Course_files\\"

tb_scraper = TutorialBarScraper()
flag = course_counter = 0
old_file = directory + "udemy_courses.txt"
present_date = datetime.datetime.now()
new_file = directory + present_date.strftime("%b") + "_" + present_date.strftime("%d") + "_Courses.txt"



def get_new_course_details(counter, course_url):
    flag=0
    titleText = headlineText = ""
    counter = counter + 1
    req = requests.get(course_url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    #print(course_url)
    titleTag = soup.find("h1", { "data-purpose" : "lead-title" })
    if titleTag == None:
        counter = counter - 1
    else:
        titleText = titleTag.text.strip()
        headlineTag = soup.find("div", { "data-purpose" : "lead-headline" })
        headlineText = headlineTag.text.strip()
        flag=1
    return flag, counter, titleText, headlineText
            
def save_new_course_details(course_number, course_website, course_title, course_description):
    if course_number==1:
        new_course_file.write(str(course_number) + ". " + course_title + "\n" + course_description +"\n" + course_website + "\n")
    else:
        new_course_file.write("\n" + str(course_number) + ". " + course_title + "\n" + course_description +"\n" + course_website + "\n")
    print(str(course_number) + ". " + course_title)
            
def get_old_course_details(file_name):
    file = open(file_name, "r", encoding="utf-8")
    file_data = file.read().split("\n")
    #print(file_data[len(file_data)-2].split())
    course_urls = []
    for i in range(len(file_data)):
        if i>0:
            if (i%4)==0:
                course_urls.append(file_data[i-1])
    #print(course_urls)
    #print("\n\n\n\n\n")
    return course_urls


old_links = get_old_course_details(old_file)
new_course_file = open(new_file, "w", encoding="utf-8")

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


while True:
    b=0
    udemy_course_links = tb_scraper.run(choice)
    for course_link in udemy_course_links:
        if  "bit.ly" in course_link:
            print("\n" + course_link + " is invalid\n")
        elif course_link in old_links:
            print("\n" + course_link + " is repeated\n")
            b=1
            break
        else:
            flag, course_counter, course_title, course_description = get_new_course_details(course_counter, course_link)
            if flag==1:
                save_new_course_details(course_counter, course_link, course_title, course_description)
    if b==1:
        break
new_course_file.close()
print("All free Courses have been successfully listed!!!")

