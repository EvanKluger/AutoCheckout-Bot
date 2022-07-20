from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = 'https://www.bestbuy.com/site/apple-airpods-with-charging-case-2nd-generation-white/6084400.p?skuId=6084400'

driver.get(url)

driver.maximize_window()
time.sleep(10)
click = driver.find_element(by=By.XPATH, value = """/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[14]/div[2]/div/div/div/button""")
click.click()
time.sleep(10)
click_to_cart = driver.find_element(by=By.XPATH, value ="""/html/body/div[7]/div/div[1]/div/div/div/div/div[1]/div[3]/a""")
click_to_cart.click()
time.sleep(10)
click_to_checkout = driver.find_element(by=By.XPATH, value ="""/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[4]/div/div[1]/button""")
click_to_checkout.click()
time.sleep(10)
continue_as_guest = driver.find_element(by=By.XPATH, value ="""/html/body/div[1]/div/section/main/div[2]/div[4]/div/div[2]/button""")
continue_as_guest.click()
time.sleep(10)
continue_to_shipping = driver.find_element(by=By.XPATH, value ="""/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/section/div[1]/div[1]/div/button""")
continue_to_shipping.click()
time.sleep(10)


time.sleep(100) 

