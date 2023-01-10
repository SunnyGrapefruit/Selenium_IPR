import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def find_pdf():
     pdf_list = []
     textarea = driver.find_elements_by_xpath("//*[contains(@href, '.pdf') or contains(@href, '.PDF')]")
     for i in textarea:
          pdf_list.append(i.get_attribute('href'))
     return pdf_list

def print_list(list):
     for i in list:
          print(i)

driver.get("https://www.cbr.ru/sitemap/")


textarea = driver.find_elements_by_xpath("//a")
link_list = []
for i in textarea:
     link = i.get_attribute('href')
     if link not in link_list and 'cbr.ru' in link:
          link_list.append(link)

link_list[10:-1] = []

all_pdf_list = []
for i in link_list:
     driver.get(i)
     all_pdf_list.extend(find_pdf())

print_list(all_pdf_list)
driver.quit()


