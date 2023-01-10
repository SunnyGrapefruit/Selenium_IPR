import json
from json import JSONEncoder

from selenium import webdriver

options = webdriver.ChromeOptions()
chrome_driver_binary = 'C:\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(chrome_driver_binary)


class Stocks:
    def __init__(self, id, name, price, link):
        self.id = id
        self.name = name
        self.price = price
        self.link = link
        #self.dividends = dividends

    def __str__(self):
        return "Stock: id = {}, name = {}, price = {}, dividends = {}".format(self.id, self.name, self.price, self.dividends) #f"Stock: id = {self.id}, name = {}self.name, price = {self.price}]"

    @staticmethod
    def pars(element):
        id_s = element.get_attribute('id')[5:]
        name = element.find_element_by_xpath('td[2]').text
        price = element.find_element_by_xpath('td[3]').text.replace('.', '').replace(',', '.')
        link = element.find_element_by_xpath('td[2]/a').get_attribute('href')
        return Stocks(id_s, name, price, link)

    def obj_dict(obj):
        return obj.__dict__

class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

link = "https://ru.investing.com/equities/russia"
driver.get(link)
all_stock = list()
root_element = driver.find_elements_by_xpath(f'//*[@id="cross_rate_markets_stocks_1"]/tbody/tr')

for i in range(5): #len(root_element)):
    curr_element = root_element[i]
    stock = Stocks.pars(curr_element)
    all_stock.append(stock)

for stock in all_stock:
    driver.get(stock.link)
    try:
        dividends = driver.find_element_by_xpath("//*[@data-test='dividend']/div/span").text.replace('.', '').replace(',', '.')
    except:
        dividends = 0
    stock.dividends = (float(dividends)/float(stock.price))*100
    print(stock)

stocks_json = json.dumps(all_stock, indent=4, cls=MyEncoder)
with open("stocks.json", "w") as my_file:
    my_file.write(stocks_json)
print('Запись завершена')

stocks_json = json.dumps(all_stock, indent=4, default=Stocks.obj_dict)
with open("stocks.json", "w") as my_file:
    my_file.write(stocks_json)
print('Запись завершена')

driver.quit()

# count_tr = driver.find_elements_by_xpath('//*[@id="cross_rate_markets_stocks_1"]//tbody//tr')
# for i in range(1, 5): #len(count_tr)+1):
#     name = driver.find_element_by_xpath(f'//*[@id="cross_rate_markets_stocks_1"]/tbody/tr[{i}]/td[2]').text
#     price = driver.find_element_by_xpath(f'//*[@id="cross_rate_markets_stocks_1"]/tbody/tr[{i}]/td[3]').text
#     link = driver.find_element_by_xpath(f'//*[@id="cross_rate_markets_stocks_1"]/tbody/tr[{i}]/td[2]/a').get_attribute('href')
#     id_s = driver.find_element_by_xpath(f'//*[@id="cross_rate_markets_stocks_1"]/tbody/tr[{i}]').get_attribute('id')[5:]
#     stock = Stocks(id_s, name, price, link)
#     all_stock.append(stock)