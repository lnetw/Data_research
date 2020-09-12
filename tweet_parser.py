#Depends on selenium package for python, selenium chrome driver, google-chrome / chrome browser
import os 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By 


#Download Chromium Driver for Selenium and place it in class path before executing this program (Link :-  https://www.seleniumhq.org/download/)
options=webdriver.ChromeOptions()

#Change the hoe directory to your user directory. This is used so as to bypass login restrictions.
#This requires user to login to twitter once so that the same login session can be used for carrying out the task
options.add_argument("--user-data-dir=/home/root/.config/chromium")
browser = webdriver.Chrome(options=options) 

#Pass the url as first argument
base_url=sys.argv[1]
browser.get(base_url)
body=browser.find_element_by_tag_name('body')
wait = ui.WebDriverWait(browser,0.5)
while True:
        try:
                wait.until(EC.visibility_of_element_located((By.XPATH,"//span[contains(@class, 'Icon Icon--large Icon--logo')]")))
                break
        except:
                body.send_keys(Keys.END)

tweets=browser.find_elements_by_class_name('tweet-text')
for tweet in tweets:
        print (tweet.text)
#Usage :- python tweet_parser.py "http://twitter.com/<remaining_url>"