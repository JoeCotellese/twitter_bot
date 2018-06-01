import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import config

class TwitterBot:
    twitter_url = 'https://www.twitter.com'
    twitter_login = twitter_url + '/login'
    twitter_logout = twitter_url + '/logout'
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
    def _setup_logger(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def login(self):
        logging.info('calling login')
        self.driver.get(self.twitter_login)
        username_field = self.driver.find_element_by_class_name('js-username-field')
        pwd_field = self.driver.find_element_by_class_name('js-password-field')
        username_field.send_keys(self.username)
        pwd_field.send_keys(self.password)
        self.driver.find_element_by_xpath('//button[text()="Log in"]').click()
        
    def logout(self):
        logging.info('calling logout')
        self.driver.get(self.twitter_logout)
        try:
            wait = WebDriverWait(self.driver, 10)
            logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Log out"]')))
            logout_button.click()
            logging.info('clicked logout')
        except TimeoutException:
            logging.info("Can't find logout button")
    def follow_who_to_follow(self, limit=20):
        if limit > 100:
            logging.info('You better be careful, more than 100 follows could get you banned')
        self.driver.get(self.twitter_url + '/who_to_follow/suggestions')
        #//*[@id="stream-item-user-237345776"]/div/div[1]/div/span/button[1]
        follow_buttons = self.driver.find_elements_by_xpath('//button[text()="Follow"]')
        for x in follow_buttons:
            print (x)

def main():
    tb = TwitterBot(config.USERNAME, config.PASSWORD)
    tb.login()
    #tb.follow_who_to_follow()
    tb.logout()

if __name__ == '__main__':
    main()