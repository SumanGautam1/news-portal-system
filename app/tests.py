from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


class TestHome(LiveServerTestCase):
    """
    Test case for the homepage and login functionality using Selenium.

    This test case automates the process of navigating to the login page, entering credentials,
    and submitting the login form. It verifies that the login process works as expected.

    Attributes:
        None
    """

    def testhomepage(self):
        """
        Tests the login functionality of the homepage.

        Steps:
            1. Launches the Chrome browser and maximizes the window.
            2. Navigates to the login page of the application.
            3. Enters the username and password into the respective fields.
            4. Clicks the login button.
            5. Waits for 5 seconds to allow the login process to complete.

        Note:
            This test assumes that the login page is accessible at 'http://127.0.0.1:8000/login/'
            and that valid credentials are provided.
        """
        # Initialize the Chrome WebDriver
        driver = webdriver.Chrome()
        driver.maximize_window()

        # Navigate to the login page
        driver.get('http://127.0.0.1:8000/login/')

        # Enter username and password
        driver.find_element(By.NAME, "username").send_keys('suman')
        driver.find_element(By.NAME, "password").send_keys('gautam')

        # Click the login button
        driver.find_element(By.XPATH, "/html/body/div/form/div[3]/button").click()

        # Wait for 5 seconds to observe the result (not recommended for production tests)
        time.sleep(5)

class TestRegister(LiveServerTestCase):
    """
    Test case for the homepage and register functionality using Selenium.

    This test case automates the process of navigating to the register page, entering credentials,
    and submitting the register form. It verifies that the register process works as expected.

    Attributes:
        None
    """

    def testregister(self):
        """
        Tests the register functionality of the homepage.

        Steps:
            1. Launches the Chrome browser and maximizes the window.
            2. Navigates to the register page of the application.
            3. Enters the username and password into the respective fields.
            4. Clicks the register button.
            5. Waits for 5 seconds to allow the register process to complete.

        Note:
            This test assumes that the register page is accessible at 'http://127.0.0.1:8000/register/'
            and that valid credentials are provided.
        """
        # Initialize the Chrome WebDriver
        driver = webdriver.Chrome()
        driver.maximize_window()

        # Navigate to the register page
        driver.get('http://127.0.0.1:8000/register/')

        # Enter details
        driver.find_element(By.NAME, "first_name").send_keys('suman')
        driver.find_element(By.NAME, "last_name").send_keys('gautam')
        driver.find_element(By.NAME, "username").send_keys('suman101')
        driver.find_element(By.NAME, "email").send_keys('suman101@gmail.com')
        driver.find_element(By.NAME, "password").send_keys('gautam123')
        driver.find_element(By.NAME, "password1").send_keys('gautam123')

        # Click the login button
        driver.find_element(By.XPATH, "/html/body/div/form/div[7]/button").click()

        # Wait for 5 seconds to observe the result (not recommended for production tests)
        time.sleep(5)

class TestFeedback(LiveServerTestCase):
    """
    Test case for the feedback functionality using Selenium.

    This test case automates the process of navigating to the feedback page, entering credentials,
    and submitting the form. It verifies that the feedback process works as expected.

    Attributes:
        None
    """

    def testfeedback(self):
        """
        Tests the feedback functionality.

        Steps:
            1. Launches the Chrome browser and maximizes the window.
            2. Navigates to the feedback page of the application.
            3. Enters the data into the respective fields.
            4. Clicks the submit button.
            5. Waits for 5 seconds to allow the process to complete.

        Note:
            This test assumes that the feedback page is accessible at 'http://127.0.0.1:8000/feedback/'
            and that valid credentials are provided.
        """
        # Initialize the Chrome WebDriver
        driver = webdriver.Chrome()
        driver.maximize_window()

        # Navigate to the feedback page
        driver.get('http://127.0.0.1:8000/feedback/')

        # Enter full name, email and description
        driver.find_element(By.NAME, "name").send_keys('suman gautam')
        driver.find_element(By.NAME, "email").send_keys('gautamsuman@gmail.com')
        driver.find_element(By.NAME, "desc").send_keys('Hello, this is from testcase.')

        # Click the submit button
        driver.find_element(By.XPATH, "/html/body/section/form/div[5]/button").click()

        # Wait for 5 seconds to observe the result
        time.sleep(5)