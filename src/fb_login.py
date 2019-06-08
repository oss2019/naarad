from selenium import webdriver
import getpass

print("Please enter your details for facebook login")

# username = input("enter you username: ")
# password = getpass.getpass("enter your password it would be hidden: ")
# Enter your password and it's safe and hidden


class Facebook:

    def __init__(self):
        self.driver = webdriver.Chrome()

        self.username = input("enter your username: ")
        self.password = getpass.getpass("enter your password: ")

    def fb_login(self):
        self.driver.get('https://www.facebook.com')  # To hit the URL
        self.driver.find_element_by_id('email').send_keys(self.username)
        self.driver.find_element_by_id('pass').send_keys(self.password)
        self.driver.find_element_by_id('loginbutton').click()

Facebook().fb_login()

