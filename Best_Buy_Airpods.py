from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


#CONSTANTS
first_name_input = input('\n What is your First Name \n')
last_name_input = input('\n What is your Last Name \n')
address_input = input('\n What is your Address \n')
#city_input = 'My City'
#zip_code_input = 'My Zip Code'




driver = webdriver.Chrome()

url = 'https://www.bestbuy.com/site/apple-airpods-with-charging-case-2nd-generation-white/6084400.p?skuId=6084400'

driver.get(url)

driver.maximize_window()
time.sleep(5)
click = driver.find_element(by=By.XPATH, value = """/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[14]/div[2]/div/div/div/button""")
click.click()
time.sleep(5)
click_to_cart = driver.find_element(by=By.XPATH, value ="""/html/body/div[7]/div/div[1]/div/div/div/div/div[1]/div[3]/a""")
click_to_cart.click()
time.sleep(5)
click_to_checkout = driver.find_element(by=By.XPATH, value ="""/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[4]/div/div[1]/button""")
click_to_checkout.click()
time.sleep(5)
continue_as_guest = driver.find_element(by=By.XPATH, value ="""/html/body/div[1]/div/section/main/div[2]/div[4]/div/div[2]/button""")
continue_as_guest.click()
time.sleep(5)
continue_to_shipping = driver.find_element(by=By.XPATH, value ="""/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/section/div[1]/div[1]/div/button""")
continue_to_shipping.click()
time.sleep(5)

First_Name = driver.find_element(By.XPATH, value ="""/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/section/div[1]/div[2]/div/div/form/div[1]/div/input""")
Last_Name = driver.find_element(By.XPATH, value ="""/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/section/div[1]/div[2]/div/div/form/div[2]/div/input""")
Address = driver.find_element(By.XPATH, value ="""/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/section/div[1]/div[2]/div/div/form/div[3]/div[2]/div/div/input""")
#City = driver.find_element(By.XPATH, value ="""/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/section/div[1]/div[2]/div/div/form/div[5]/div[1]/div/input""")
#Zip_Code = driver.find_element(By.XPATH, value ="""/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/section/div[1]/div[2]/div/div/form/div[6]/div/div[1]/div/input""")

First_Name.send_keys(first_name_input)
Last_Name.send_keys(last_name_input) 
Address.send_keys(address_input) 

time.sleep(10)

Address_Suggested = driver.find_element(By.XPATH, value ="""/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/section/div[1]/div[2]/div/div/form/div[3]/div[2]/div/div/div/div""")
Address_Suggested.click() 
#City.send_keys(city_input) 
#Zip_Code.send_keys(zip_code_input) 


time.sleep(100) 

