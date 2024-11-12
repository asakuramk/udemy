from jwt.utils import bytes_to_number

url="https://192.168.1.103:6150/?onepasswdfill=E393059F71954B619ED7E87023B37F10&onepasswdvault=FFDAE69715284BD8AC3CE978276A0485#/signin"
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

sleep(2)
login_button = driver.find_element(By.XPATH, value='//*[@id="details-button"]')
login_button.click()

sleep(2)
login_button = driver.find_element(By.XPATH, value='//*[@id="proceed-link"]')
login_button.click()


sleep(2)
base_window = driver.window_handles[0]
# fb_login_window = driver.window_handles[1]
# driver.switch_to.window(fb_login_window)
# print(driver.title)



IDinput = driver.find_element(By.XPATH, value='//*[@id="dsm-user-fieldset"]/div/div/div[1]/input')
# password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
IDinput.send_keys(ID)
# password.send_keys(PW)
# password.send_keys(Keys.ENTER)
login_button = driver.find_element(By.XPATH, value='//*[@id="sds-login-vue-inst"]/div/span/div/div[2]/div[2]/div/div[3]/div[2]/div/div[2]/div[3]/div[1]')
login_button.click()



sleep(2)
PWinput = driver.find_element(By.XPATH, value='//*[@id="dsm-pass-fieldset"]/div[1]/div/div[1]/input')
# password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
PWinput.send_keys(PW)
# password.send_keys(PW)
# password.send_keys(Keys.ENTER)
login_button = driver.find_element(By.XPATH, value='//*[@id="sds-login-vue-inst"]/div/span/div/div[2]/div[2]/div/div[3]/div[2]/div/div[2]/div[1]/div[3]/div[1]')
login_button.click()
# ここまでOK




driver.switch_to.window(base_window)
print(driver.title)

sleep(5)

allow_location_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

notifications_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

cookies = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()
