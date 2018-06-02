import logging
from time import sleep
from urllib.parse import quote
import arrow
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.keys import Keys
from twitter_bot.parseprofile import ParseProfile
from twitter_bot.helper import StreamList
from twitter_bot.storage import Storage


class TwitterBot:
    twitter_url = 'https://www.twitter.com'
    twitter_login = twitter_url + '/login'
    twitter_logout = twitter_url + '/logout'
    twitter_suggestions = twitter_url + '/who_to_follow/suggestions'
    def __init__(self, username, password):
        self._setup_logger()
        logging.info('initializing TwitterBot for %s' % username)
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()
        self.storage = Storage('twitterbot.db')

    def _setup_logger(self):
        logging.basicConfig(filename='twitterbot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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
            logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(., 'Log out')]")))
            logout_button.click()
            logging.info('clicked logout')
        except TimeoutException:
            logging.info("Can't find logout button")
        self.driver.close()

    def follow_user(self, url):
        try:
            self.driver.get(url)
            source = self.driver.page_source
            profile = ParseProfile(source)
            th = profile.twitter_handle
            logging.info("trying to follow %s" % th)
            if (profile.following == False):
                logging.info("following {}".format(th))
                follow_button = self.driver.find_element_by_css_selector('button.follow-text')
                actions = ActionChains(self.driver)
                actions.move_to_element(follow_button)
                actions.wait(1)
                actions.click()
                actions.wait(1)
                actions.perform()
                self.storage.save_user(th)
                sleep(3)
                return True
            else:
                logging.info("already following {}".format(profile.twitter_handle))
                sleep(3)
                return False        
        except WebDriverException as e:
            logging.exception("WebDriverException in follow_user")
            return False
        except AttributeError as e:
            logging.exception("Attribute Error in follow_user")
            return False
    
    def _expand_endless_scroll(self):
        for i in range(1,20):
            self.driver.execute_script("window.scrollTo(0,   document.body.scrollHeight);")
            sleep(5)
    
    def unfollow_user(self, url):
        self.driver.get(url)
        source = self.driver.page_source
        profile = ParseProfile(source)
        th = profile.twitter_handle
        logging.info("calling unfollow_user")
        if (profile.follows_back == False):            
            logging.info("unfollowing %s" % th)
            unfollow_button = self.driver.find_element_by_css_selector('button.following-text')
            actions = ActionChains(self.driver)
            actions.move_to_element(unfollow_button).click().perform()
            sleep(10)
        else:
            logging.info ("not unfollowing %s - they follow you back" % th)
    
    def follow_suggested_followers(self, count):
        logging.info("following suggested followers")
        self.driver.get(self.twitter_suggestions)
        source = self.driver.page_source
        stream_list = StreamList(source).profile_links
        follow_count = 0
        for url in stream_list:
            if self.follow_user(url) == True:
                follow_count+=1
            if follow_count >= count:
                logging.info("you've hit your follow limit of %s" % follow_count)
                break
    
    def follow_search(self, count, search):
        logging.info("following people who've tweeted about %s" % search)
        url = 'https://twitter.com/search?q={}'.format(quote(search))
        self.driver.get(url)
        self._expand_endless_scroll()
        source = self.driver.page_source
        stream_list = StreamList(source).profile_links
        follow_count = 0
        for url in stream_list:
            if self.follow_user(url) == True:
                follow_count+=1
            if follow_count >= count:
                logging.info("you've hit your follow limit of %s" % follow_count)
                break
        
        
