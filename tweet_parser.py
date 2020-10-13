# Depends on selenium package for python, selenium chrome driver, google-chrome / chrome browser
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

gecko = os.path.normpath(r'C:\Users\Max\PycharmProjects\Prect1\venv\Lib\site-packages\selenium\geckodriver.exe')
binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
browser = webdriver.Firefox(firefox_binary=binary, executable_path=gecko)
base_url = "https://twitter.com/search?q=from%3AXbox%20%20since%3A2016-11-20%20until%3A2016-11-28&src=typd&lang=en"
# http://twitter.com/feministki
# Pass the url as first argument
# base_url=sys.argv[1]
browser.get(base_url)
body = browser.find_element_by_tag_name('body')
# wait = ui.WebDriverWait(browser, 0.5)
# while True:
#     try:
#         wait.until(
#             EC.visibility_of_element_located((By.XPATH, "//span[contains(@class, 'Icon Icon--large Icon--logo')]")))
#         break
#     except:
#         body.send_keys(Keys.END)

tweets = browser.find_element_by_css_selector('#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-yfoy6g.r-18bvks7.r-1ljd8xs.r-13l2t4g.r-1phboty.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div:nth-child(2) > div > div > section > div > div > div:nth-child(1) > div > div > article > div > div > div > div.css-1dbjc4n.r-18u37iz > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1mi0q7o > div:nth-child(2) > div:nth-child(1) > div > span:nth-child(3)')
print(tweets)
# for tweet in tweets:
#     print(tweet.text)
# Usage :- python tweet_parser.py "http://twitter.com/<remaining_url>"