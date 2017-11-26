import socket
from urllib.parse import urlparse

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import override_settings, tag

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@tag('selenium')
@override_settings(ALLOWED_HOSTS=['*'])
class BaseTestCase(StaticLiveServerTestCase):
    """
    Provides base test class which connects to the Docker
    container running selenium.
    """
    host = '0.0.0.0'

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.host = socket.gethostbyname(socket.gethostname())
        cls.selenium = webdriver.Remote(
            command_executor='http://selenium:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME,
        )
        cls.selenium.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()


class AdminTest(BaseTestCase):
    fixtures = ['users']

    def test_login(self):
        """
        As a superuser with valid credentials, I should gain
        access to the Django admin.
        """
        self.selenium.get(self.live_server_url)
        username_input = self.selenium.find_element_by_name('username')
        username_input.send_keys('george')
        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('password1234')
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()

        path = urlparse(self.selenium.current_url).path
        self.assertEqual('/', path)

        body_text = self.selenium.find_element_by_tag_name('body').text
        self.assertIn('WELCOME, GEORGE.', body_text)
