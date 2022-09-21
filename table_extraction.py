
import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

url="https://prosettings.net/valorant-pro-settings-gear-list/"
driver.get(url)
driver.implicitly_wait(5)
sleep(5)
#accept cookies
# try:
    # driver.find_element(By.ID, 'L2AGLb').click()
    # print('Accepting coockies')
# except:
    # pass

xpath='//*[@id="table_1_wrapper"]/table/thead/tr[1]/th'
#elements = linkedin_urls = driver.find_elements_by_xpath('//div[@class="yuRUbf"]//a[contains(@href,"https://uk.linkedin.com")]')
headers = driver.find_elements(by=By.XPATH, value=xpath)
h_text=[h.text for h in headers]
print(h_text)

xpath='//*[@id="table_1_wrapper"]/table/tbody/tr'
#elements = linkedin_urls = driver.find_elements_by_xpath('//div[@class="yuRUbf"]//a[contains(@href,"https://uk.linkedin.com")]')
rows = driver.find_elements(by=By.XPATH, value=xpath)
n_rows=len(rows)

xpath='//*[@id="table_1_wrapper"]/table/tbody/tr[3]/td'
#elements = linkedin_urls = driver.find_elements_by_xpath('//div[@class="yuRUbf"]//a[contains(@href,"https://uk.linkedin.com")]')
cols = driver.find_elements(by=By.XPATH, value=xpath)
n_cols=len(cols)

print(n_rows,n_cols)

data=[]
now = datetime.now()
dt_string = now.strftime("%Y_%m_%d %H_%M_%S")
f='output'+dt_string+'.csv'
with open(f, 'wt', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter='	',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(h_text)
    for rn in range(n_rows):
        xpath='//*[@id="table_1_wrapper"]/table/tbody/tr['+str(rn+1)+']/td'
        row = driver.find_elements(by=By.XPATH, value=xpath)
        row_text=[e.text for e in row]
        print(row_text)
        data+=[row_text]
        spamwriter.writerow(row_text)