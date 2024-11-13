from jwt.utils import bytes_to_number

url="https://gofile.me/76q2x/UnLUkCrd4"
ID="tablet"
PW="Jyt=og"



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

# FB_EMAIL = YOUR FACEBOOK LOGIN EMAIL
# FB_PASSWORD = YOUR FACEBOOK PASSWORD

driver = webdriver.Chrome()

driver.get(url)

sleep(5)
login_button = driver.find_element(By.XPATH, value='//*[@id="ext-gen43"]')
login_button.click()
