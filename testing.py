import requests
from bs4 import BeautifulSoup

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
    
links1 = ['https://www.udemy.com/course/python-and-flask-only-demonstration-course/?couponCode=9A8C8BBD15AE6B547376', 'https://www.udemy.com/course/python-for-beginners-course-in-depth/?couponCode=B1E815983D38C6A4715A', 'https://www.udemy.com/course/the-complete-beginners-guide-to-the-arduino/?couponCode=27CCD9DC12A6C6BC8219', 'https://www.udemy.com/course/weka30mins/?couponCode=B823927D389567757AD3', 'https://www.udemy.com/course/certified-kubernetes-administrator-course/?couponCode=TRY10FREE404', 'https://www.udemy.com/course/ultimate-ethical-hacking/?couponCode=FREE4HACKERS', 'https://www.udemy.com/course/sapob52okp1/?couponCode=FAF1AAA04627DE78AAFC', 'https://www.udemy.com/course/agile-scrum-in-depth-guide-simulation-and-best-practices/?couponCode=DA34D463FC3C328F4103', 'https://www.udemy.com/course/network-protocol-ethical-hacking-course/?couponCode=HULAKK', 'https://www.udemy.com/course/learn-and-understand-buffer-overflow-from-scratch-beginner/?couponCode=BFPU12', 'https://www.udemy.com/course/learn-and-understand-ethical-hacking-from-scratch/?couponCode=58-ERT', 'https://www.udemy.com/course/complete-vmware-vsphere-esxi-and-vcenter-administration/?couponCode=ONETIMEONLY']

links2 = ['https://www.udemy.com/course/easy-learning-c-for-beginners/?couponCode=997232B6356082E41670', 'https://www.udemy.com/course/the-complete-introduction-to-the-deep-web/?couponCode=DF8527E5D38DAEB4B6B5', 'https://www.udemy.com/course/mastering-coding-interviews-and-competitions/?couponCode=ALGOSTEMFREE', 'https://www.udemy.com/course/advanced-cyber-security-malware-hacking-course/?couponCode=JONAJ1A', 'https://www.udemy.com/course/cyber-security-kali-linux-course/?couponCode=IGNA128', 'https://www.udemy.com/course/the-certified-ethical-hackingceh-course-2020/?couponCode=BKVETA', 'https://www.udemy.com/course/security-awareness-for-everyone/?couponCode=7D3DE0D416E938C04EC7', 'https://www.udemy.com/course/google-cloud-professional-data-engineer-get-certified/?couponCode=0AE519024C29A8F1CA81', 'https://www.udemy.com/course/python-for-pentesters/?couponCode=GROWASKILL', 'https://www.udemy.com/course/advanced-zoom/?couponCode=AZOOMFREE', 'https://www.udemy.com/course/scrum-master-one-training-2020/?couponCode=NOVFREE', 'https://www.udemy.com/course/network-ethical-hacking/?couponCode=27750B6C891CC8B6D005']

links3 = ['https://www.udemy.com/course/sap-fico-for-beginners-with-simple-and-detailed-explanation/?couponCode=FREECOURSE', 'https://www.udemy.com/course/google-certified-professional-cloud-architect-practice-tests-h/?couponCode=60F21BA60F9D476D2612', 'https://www.udemy.com/course/power-bi-master-course/?couponCode=C83D916C6D59F710B22A', 'https://www.udemy.com/course/ai-900-microsoft-azure-ai-fundamentals-practice-sets/?couponCode=NOV2020', 'https://www.udemy.com/course/python-complete-course-for-beginners/?couponCode=478116E21A888DFDCF29', 'https://www.udemy.com/course/guia-oficial-de-scrum-narrada-en-espanol/?couponCode=NOV2020', 'https://www.udemy.com/course/milestones-in-python-38-with-exciting-new-features/?couponCode=MILESTONE.FREEBIES', 'https://www.udemy.com/course/master-en-un-solo-curso-iso-27001/?couponCode=NOV2020', 'https://www.udemy.com/course/kanban-fundamentos-certificacion/?couponCode=NOV2020', 'https://www.udemy.com/course/fast-track-to-ml-datascience-steganography/?couponCode=BEE6000A4CE76B22D68E', 'https://www.udemy.com/course/super-way-to-learn-arduino-creative/?couponCode=ROBOT11OMG', 'https://www.udemy.com/course/hands-on-python3-regular-expression-2020/?couponCode=0E676A889BA3CAEAE08C']

all_links = links1 + links2 + links3

count = 1
url = all_links[0]
print(url)
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')
url_body = soup.get_text()
#s = soup.find(class='udlite-text-md clp-lead__headline')
headline_tag = soup.find("div", { "class" : "udlite-text-md clp-lead__headline" })
print(headline_tag.text.strip())
#headline_elements = headline_tag.split(">")

#print(soup.div.udlite-text-md-clp-lead__headline)
###print(soup.prettify())


"""print(url_body)
udemy_formatted_body = url_body.split("\n",5)
title = udemy_formatted_body[4]
if '|' in title:
    updated_title = title.split("|")
    print(str(count) + ". " + updated_title[0])
else:
    print(str(count) + ". " + title)
print(url)
print()
count = count + 1"""


