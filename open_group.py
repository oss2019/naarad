import getpass
from selenium import webdriver

print("Please enter your details for facebook login")


class Facebook:

    def __init__(self):
        self.username = input("enter your username: ")
        self.password = getpass.getpass("enter your password: ")
        self.link = input("enter the link:")
        self.driver = webdriver.Chrome()
        self.fb_login()

    def open_group(self, input_link):
        self.driver.get(input_link)

    def fb_login(self):
        self.driver.get("https://www.facebook.com/")
        self.driver.find_element_by_id('email').send_keys(self.username)
        self.driver.find_element_by_id('pass').send_keys(self.password)
        self.driver.find_element_by_id('loginbutton').click()
        self.open_group(self.link)

Facebook()
