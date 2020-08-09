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

#set to Firefox, direct to Roobet.com, and wait for element
driver = Firefox(options=opts)
driver.get('https://roobet.com/crash')
driver.implicitly_wait(20)

#search for parent 'jss107' tag and grab all inner attributes
search_form = driver.find_element_by_class_name("jss107")
search_form2 = search_form.find_element_by_class_name('MuiButton-label')
#print(search_form.get_attribute('innerHTML'))


# write to file for Java input
f = open("crashData.txt","w+")
f.write(search_form.get_attribute('innerHTML'))
f.close()

driver.quit()
