from base.base import BaseObject
from selenium.webdriver.common.by import By
from config import URL

class CheckboxesScrollPage(BaseObject):

    CHECKBOXES_SCROLL_PAGE_URL = URL.CHECKBOXES_AND_SCROLL_URL
    SELECT_BTN = (By.CLASS_NAME, 'dropdown')
    SECTION_BTN = (By.XPATH, '//a[@href="checkbox-and-scroll.html"]')
    CHECKBOX_LIST = (By.XPATH, "//ul[@class='checkbox-list']//input[@type='checkbox']")
    CHECKBOX_COUNTER = (By.ID, "counter")
    BACK_BTN = (By.CLASS_NAME, 'back-button')


    def __init__(self, driver):
        super().__init__(driver)

    def open_section(self):
        self.driver.get(self.CHECKBOXES_SCROLL_PAGE_URL)

    def __get_all_checkboxes(self):
        return self.get_all_elements_located(self.CHECKBOX_LIST)

    def __enable_checkbox(self, count_checkbox_to_enable):
        checkboxes = self.__get_all_checkboxes()
        enabled_checkboxes = []
        i = 0
        for checkbox in checkboxes:
            if i == count_checkbox_to_enable:
                break

            self.click(checkbox)
            enabled_checkboxes.append(checkbox)
            i += 1
        return enabled_checkboxes

    def enable_and_disable_checkbox(self,count_checkbox_to_enable, checkboxes_to_disable):
        enabled_checkboxes = self.__enable_checkbox(count_checkbox_to_enable)
        i = 0
        for checkbox in enabled_checkboxes:
            if i == checkboxes_to_disable:
                break

            self.click(checkbox)
            i += 1

    def get_checkbox_counter(self):
        return self.get_text(self.CHECKBOX_COUNTER)
