from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from helper.assertions import Assertions
from selenium.webdriver import ActionChains
from helper.decorators import Decorator
from helper.digits_utils import DigitsUtils


class BaseObject:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)
        self.assertions = Assertions
        self.digits_utils = DigitsUtils
        self.decorator = Decorator
        self.actions = ActionChains(self.driver)

    def _get_visible(self, locator, timeout=None) -> WebElement:
        if timeout is None:
            return self.wait.until(ec.visibility_of_element_located(locator))
        else:
            return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def _get_visibility_of_all_elements_safe(self, locator, timeout=None):
        if timeout is None:
            try:
               return self.wait.until(ec.visibility_of_all_elements_located(locator))
            except TimeoutException:
                return []
        else:
            try:
                return WebDriverWait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))
            except TimeoutException:
                return []

    def _get_clickable(self, locator, timeout=None):
        if timeout is None:
            return self.wait.until(ec.element_to_be_clickable(locator))
        else:
            return WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    def is_not_clickable(self, locator, timeout=None):
        if timeout is None:
            try:
                self.wait.until(ec.element_to_be_clickable(locator))
                raise AssertionError("The element is clickable")
            except TimeoutException:
                return True
        else:
            try:
                WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator))
                raise AssertionError("The element is clickable")
            except TimeoutException:
                return True

    def is_not_visible(self, locator, timeout=None):
        if timeout is None:
            try:
                self.wait.until(ec.visibility_of_element_located(locator))
                raise AssertionError("The element is visible")
            except TimeoutException:
                return True
        else:
            try:
                WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
                raise AssertionError("The element is visible")
            except TimeoutException:
                return True

    def click(self, locator):
        self._get_clickable(locator).click()

    def send_keys(self, locator, text):
        self._get_visible(locator).send_keys(text)

    def get_current_url(self):
        return self.driver.current_url

    def get_text(self, locator):
        return self._get_visible(locator).text

    def get_texts_of_all_elements(self, locator, timeout=None):
        elements = self._get_visibility_of_all_elements_safe(locator, timeout)
        texts = []
        for element in elements:
            texts.append(element.text)
        return texts

    def get_css_property(self, locator, property_name):
        return self._get_visible(locator).value_of_css_property(property_name)

    def hover(self, locator):
        self.actions.move_to_element(self._get_visible(locator)).perform()

    def get_all_elements_located(self, locator, timeout=None):
        if timeout is None:
            return self.wait.until(ec.visibility_of_all_elements_located(locator))
        else:
            return WebDriverWait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))

    def clear_backspace(self, locator):
        self.click(locator)
        self._get_visible(locator).send_keys(Keys.BACKSPACE)

    def clear(self, locator):
        self._get_visible(locator).clear()

    def drag_and_drop(self, source, target):
        self.actions.drag_and_drop(source, target).perform()

    def scroll_element_by_step(self, locator, step, scroll_up=False):
        element = self._get_visible(locator)

        if scroll_up:
            self.driver.execute_script("arguments[0].scrollTop -= arguments[1];", element, step)
        else:
            self.driver.execute_script("arguments[0].scrollTop += arguments[1];", element, step)

    def scroll_to_element(self, locator):
        self.actions.scroll_to_element(self._get_visible(locator)).perform()

    def get_input_or_output_text(self, locator):
        return self._get_visible(locator).get_attribute("value")


