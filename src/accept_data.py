from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import getpass

print("Please enter your details for facebook login")


class Facebook:

    def __init__(self):
        self.fb_details()
        self.group_details()
        self.info()

    def fb_details(self):
        self.username = input("enter your username: ")
        self.password = getpass.getpass("enter your password: ")

    def group_details(self):
        self.group = input("please enter group pages URL \
        seperated through ',' : ")
        self.group = self.group.split(',')

    def info(self):
        self.message = input("please enter a description")
        self.path = input("please tell the full path of Image/Video: ")

    def group_pages(self):
        for i in range(len(self.group)):
            self.link = self.group[i]
            self.driver.get(self.link)
            self.description()
            # self.image()
            self.publish()

    def description(self):
        description_box = /
        self.driver.find_element(By.XPATH, "//*[@name='xhpc_message_text']")
        time.sleep(5)
        description_box.send_keys(self.message)
        time.sleep(5)

    def image(self):
        media_button = self.driver.find_element_by_xpath('.//*[@id="js_i"]')
        time.sleep(3)
        media_button._execute(Command.CLICK_ELEMENT)
        time.sleep(5)
        upload_photo = self.driver.find_element_by_xpath(
            "//*[@data-testid='media-attachment-add-photo']")
        upload_photo.send_keys(self.path)
        time.sleep(5)

    def publish(self):
        buttons = self.driver.find_elements_by_tag_name('button')
        for button in buttons:
            if button.text == 'Post':
                button.click()

    def fb_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.facebook.com/")
        self.driver.find_element_by_id('email').send_keys(self.username)
        self.driver.find_element_by_id('pass').send_keys(self.password)
        self.driver.find_element_by_id('loginbutton').click()
        self.group_pages()


Facebook().fb_login()
