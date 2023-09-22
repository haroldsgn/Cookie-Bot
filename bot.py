from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:\development\chromedriver-win64\chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

# money
cursor_price = int(driver.find_element(By.ID, 'buyCursor').text.split()[2])
grandma_price = int(driver.find_element(By.ID, 'buyGrandma').text.split()[2])
factory_price = int(driver.find_element(By.ID, 'buyFactory').text.split()[2])
mine_price = int(driver.find_element(By.ID, "buyMine").text.split()[2].replace(",", ""))
shipment_price = int(driver.find_element(By.ID, "buyShipment").text.split()[2].replace(",", ""))
alchemy_price = int(driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]').text.split()[3].replace(",", ""))
portal_price = int(driver.find_element(By.ID, "buyPortal").text.split()[2].replace(",", ""))
time_machine_price = int(driver.find_element(By.XPATH, '//*[@id="buyTime machine"]').text.split()[3].replace(",", ""))
cookies_second = driver.find_element(By.ID, "cps").text


timeout = time.time() + 5
five_min = time.time() + 60*5  # 5minutes

while True:
    cookie.click()

    available_money = driver.find_element(By.ID, "money").text
    if "," in available_money:
        available_money = driver.find_element(By.ID, "money").text.replace(",", "")
    available_cookies = int(available_money)

    if time.time() > timeout:
        if available_cookies >= time_machine_price:
            buy_time_machine = driver.find_element(By.XPATH, '//*[@id="buyTime machine"]/b')
            buy_time_machine.click()

        elif available_cookies >= portal_price:
            buy_portal = driver.find_element(By.XPATH, '//*[@id="buyPortal"]/b')
            buy_portal.click()

        elif available_cookies >= alchemy_price:
            buy_alchemy = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]/b')
            buy_alchemy.click()

        elif available_cookies >= shipment_price:
            buy_shipment = driver.find_element(By.XPATH, '//*[@id="buyShipment"]/b')
            buy_shipment.click()

        elif available_cookies >= mine_price:
            buy_mine = driver.find_element(By.XPATH, '//*[@id="buyMine"]/b')
            buy_mine.click()

        elif available_cookies >= factory_price:
            buy_factory = driver.find_element(By.XPATH, '//*[@id="buyFactory"]/b')
            buy_factory.click()

        elif available_cookies >= grandma_price:
            buy_grandma = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]/b')
            buy_grandma.click()

        elif available_cookies >= cursor_price:
            buy_cursor = driver.find_element(By.XPATH, '//*[@id="buyCursor"]/b')
            buy_cursor.click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cookies_x_second = driver.find_element(By.ID, "cps").text
        print(cookies_x_second)
        five_min = time.time() + 60 * 5
