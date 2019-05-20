from selenium import webdriver
import getpass

print("Please enter your details for facebook login")
# username = input("enter you username: ")
# password = getpass.getpass("enter your password it would be hidden: ")
# Enter your password and it's safe and hidden

  # To open the web browser(google chrome)


class Facebook:

    def __init__(self,username,password):
        self.username = input("enter your username: ")
        self.password = getpass.getpass("enter your password: ")

    def fb_login(self):
        driver = webdriver.Chrome()
        driver.get('https://www.facebook.com')  # To hit the URL
        driver.find_element_by_id('email').send_keys(username)
        driver.find_element_by_id('pass').send_keys(password)
        driver.find_element_by_id('loginbutton').click()

Facebook.fb_login(username,password)