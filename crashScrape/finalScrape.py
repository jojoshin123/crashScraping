#from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

#set browser to headless
opts = Options()
opts.headless = True
assert opts.headless

#set to Firefox and direct to Roobet.com
driver = Firefox(options=opts)
driver.get('https://roobet.com/crash')
driver.implicitly_wait(20)
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "jss107"))
#     )
# finally:
#     driver.quit()

#search for parent 'jss107' tag and grab all inner attributes
search_form = driver.find_element_by_class_name("jss107")
search_form2 = search_form.find_element_by_class_name('MuiButton-label')
print(search_form.get_attribute('innerHTML'))

driver.quit()
