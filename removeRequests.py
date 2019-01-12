from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.common.actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from math import ceil
import time

f = open('facebook.txt', 'r')
if f.mode is not 'r':
    exit()

f = f.readlines()
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(chrome_options=chrome_options)

browser.get('https://www.facebook.com/friends/requests/?fcref=jwl&outgoing=1')
elem = browser.find_element_by_name('email')
elem.click()
elem.send_keys(f[0][:-1])
elem = browser.find_element_by_name('pass')
elem.click()
elem.send_keys(f[1] + Keys.ENTER)
num = ceil((int(f[2])) / 10) + 1
while (num is not 0):
    try:
        elem = WebDriverWait(browser, 2.5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="js_36"]')))
        elem.click()
        num -= 1
    except:
        break



browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
num = int(f[2])
sentButtons = browser.find_elements(By.CSS_SELECTOR, '._42ft._4jy0.FriendRequestOutgoing.enableFriendListFlyout.outgoingButton.enableFriendListFlyout._4jy3._517h._51sy')

for i in range(num):
    try:
        time.sleep(2.5)
        elem = sentButtons[i]
        ActionChains(browser).move_to_element(elem).perform()
        time.sleep(0.5)
        elem = browser.find_element_by_css_selector('.uiMenuItem.FriendListCancel')
        ActionChains(browser).move_to_element(elem).click().perform()
        elem = WebDriverWait(browser, 2.5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '._42ft._42fu.layerConfirm.uiOverlayButton.selected._42g-._42gy')))
        elem.click()

    except:
        
        break


print('done')
time.sleep(100)
browser.quit()