from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import re
import time

cdp = "/usr/bin/chromedriver"

service = Service(cdp)

driver = webdriver.Chrome(service=service)
driver.get('https://github.com/usernam121/')
repo = 'https://github.com/usernam121'
res = driver.find_elements(By.CLASS_NAME, "repo")
# time.sleep(2)
links = []
flinks = []

def loop(next_page):
    driver.get(next_page)
    res2 = driver.find_elements(By.CLASS_NAME, 'Link--primary')
    for a in res2:
        pass

    if 'py' in a.text:
        secnd_page = f"{repo}/{l}/blob/main/{a.text}"
        print("yo shit worked gng")
        mainpage_link = driver.get(secnd_page)
        source = driver.find_element(By.TAG_NAME, 'Body')
        if re.search(r"\bpassword\b", source.text, re.IGNORECASE):
            print(f"found da pass at: {secnd_page}")
        else:
            print(f"no password found at: {secnd_page}")
    time.sleep(2)




for i in res:
    links.append(i.text)
# print(links)

for l in links:
    next_page = f"{repo}/{l}"
    flinks.append(next_page)
    loop(next_page)
# print(flinks)
driver.quit()
