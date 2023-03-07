from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
#from selenium import webdriver
#import subprocess



#s = Service('/usr/local/bin/geckodriver')
#options = webdriver.FirefoxOptions()
options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument("--incognito")

driver = webdriver.Remote( 
command_executor="http://138.25.33.132:4444",
options=options

#options = webdriver.ChromeOptions()
)

#driver = webdriver.Firefox(options=options)

driver.get('https://lx.uts.edu.au/')

try:

    driver.find_element(By.XPATH, "//a[contains(text(),'LX Resources')]").click()
    driver.find_element(By.XPATH, "//a[contains(text(),'Inclusive and accessible practices')]").click()
    driver.find_element(By.XPATH, "//div[@id='ld-expand-253085']/div/a/div[2]").click()
    driver.find_element(By.XPATH, "//div[@id='learndash_post_253085']/div/div[3]/div[3]/a/span").click()
    driver.find_element(By.XPATH, "//a[contains(text(),'LX.lab')]").click()
    driver.find_element(By.XPATH, "//a[contains(text(),'LX Blog')]").click()
    driver.find_element(By.XPATH, "//main[@id='main']/section[4]/div/div[2]/div/div[2]/div/div[3]/a").click()
    driver.find_element(By.XPATH, "//img[@alt='UTS-header']").click()
    driver.find_element(By.XPATH, "//main[@id='main']/div/div[2]/section/div/div/button[2]").click()
    driver.find_element(By.XPATH, "//a[contains(text(),'opener')]").click()
    driver.find_element(By.ID, "s").click()
    driver.find_element(By.ID, "s").send_keys('careers')
    driver.find_element(By.CSS_SELECTOR, ".search-form").submit()
    driver.implicitly_wait(10) # seconds
    driver.find_element(By.XPATH, "//a[contains(text(),'Tools for threading WIL into your whole of course design: Careers Canvas modules and the TRACK-Learner tool | 12 October')]").click()

finally: 
    driver.quit()
