from base.base import BaseObject
from selenium.webdriver.common.by import By

class ValueValidatePage(BaseObject):

    VALUE_FIELD = (By.ID, "dataInput")
    VALIDATION_SQUARE = (By.ID, "validationSquare")
    SELECT_BTN = (By.CLASS_NAME, "dropdown")
    VALIDATION_SECTION_BTN = (By.XPATH, "//a[@href='check_and_validate.html']")
    PROPERTY_NAME_COLOR = "background-color"
    BACK_BTN = (By.CLASS_NAME, "back-button")


    def __init__(self, url, driver):
        super().__init__(driver)
        self.url = url

    def open_section(self):
        self.driver.get(self.url)

    def enter_value(self, value):
        self.send_keys(self.VALUE_FIELD, value)

    def get_message(self):
        return self.get_text(self.VALIDATION_SQUARE)

    def get_color(self):
        return self.get_css_property(self.VALIDATION_SQUARE, self.PROPERTY_NAME_COLOR)


