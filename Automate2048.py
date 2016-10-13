import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://gabrielecirulli.github.io/2048/')

htmlElem = browser.find_element_by_tag_name('body')
exitPoint = browser.find_element_by_class_name('game-message')

while exitPoint.text == '': 

    htmlElem.send_keys(Keys.RIGHT)
    time.sleep(2)
    htmlElem.send_keys(Keys.UP)
    time.sleep(2)
    htmlElem.send_keys(Keys.DOWN)
    time.sleep(2)
    htmlElem.send_keys(Keys.LEFT)
    time.sleep(2)

Score = browser.find_element_by_class_name('score-container')

print('Your Score: %s' % (Score.text))

print('GAME OVER!!!')

browser.quit()

