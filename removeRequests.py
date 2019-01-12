from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.common.actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import ceil
import time

# open data file, make sure valid and then get all the lines of the file
f = open('facebook.txt', 'r')
if f.mode is not 'r':
    exit()
f = f.readlines()

# disable notifications so that if it says "Facebook wants to know your location", dialog box won't show up
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

# initializing web-driver
browser = webdriver.Chrome(chrome_options=chrome_options)

# go to the webpage showing the outgoing friend requests
browser.get('https://www.facebook.com/friends/requests/?fcref=jwl&outgoing=1')

# type in email
elem = browser.find_element_by_name('email')
elem.click()
elem.send_keys(f[0][:-1]) # removed last character to not have the '\n' at the end

# type in password
elem = browser.find_element_by_name('pass')
elem.click()
elem.send_keys(f[1] + Keys.ENTER)

# convert approximate number of friend requests to how many times the "show more requests" buttom must be clicked
numTimes = ceil((int(f[2])) / 10) + 1
while (numTimes is not 0):
    # have a try, except framework to not have to deal with a failure to find more buttons
    try:
        # waiting 2.5 seconds each time to get new button to show more friends
        elem = WebDriverWait(browser, 2.5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.pam.uiBoxLightblue._5cz.uiMorePagerPrimary')))
        elem.click()
        numTimes -= 1
    except:
        break

# get to top of the page so that we can hover over the Friend Request Sent Button
browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)

# get all the Friend Request Sent Buttons
sentButtons = browser.find_elements(By.CSS_SELECTOR, '._42ft._4jy0.FriendRequestOutgoing.enableFriendListFlyout.outgoingButton.enableFriendListFlyout._4jy3._517h._51sy')
numRequests = len(sentButtons)

# go through all the buttons
for i in range(numRequests):
    # get current button
    elem = sentButtons[i]

    # hover over current button
    ActionChains(browser).move_to_element(elem).perform()
    
    # click Cancel Friend Request and then click OK button
    elem = WebDriverWait(browser, 2.0).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.uiMenuItem.FriendListCancel')))
    ActionChains(browser).move_to_element(elem).click().perform()
    elem = WebDriverWait(browser, 2.5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '._42ft._42fu.layerConfirm.uiOverlayButton.selected._42g-._42gy')))
    elem.click()
    
    # have to wait until current cancelation is finished to go to next one
    time.sleep(2.5)


print('done')
time.sleep(100)
browser.quit()