from base.base import BaseObject
from selenium.webdriver.common.by import By
from config import URL

class InputClickPage(BaseObject):

    INPUT_AND_CLICK_URL = URL.INPUT_AND_CLICK_URL
    SELECT_BTN = (By.CLASS_NAME, 'dropdown')
    SECTION_BTN = (By.XPATH, '//a[@href="input-and-click.html"]')
    VALUE_FIELD = (By.ID, 'inputText')
    ADD_BTN = (By.ID, 'addBtn')
    DELETE_BTN = (By.ID, 'deleteBtn')
    BACK_BTN = (By.CLASS_NAME, 'back-button')
    ITEM_IN_CONTAINER = (By.CLASS_NAME, 'item')

    def __init__(self, driver):
        super().__init__(driver)

    def open_section(self):
        self.driver.get(self.INPUT_AND_CLICK_URL)

    def _enter_value(self, value):
        self.send_keys(self.VALUE_FIELD, value)

    def __add_value(self, value):
        self._enter_value(value)
        self.click(self.ADD_BTN)

    def add_values(self, values):
        for value in values:
            self.__add_value(value)

    def delete_values(self, delete_count):
        i = 0
        while i < delete_count:
            self.click(self.DELETE_BTN)
            i += 1

    def get_text_all_added_values(self):
        return self.get_texts_of_all_elements(self.ITEM_IN_CONTAINER)



