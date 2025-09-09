from base.base import BaseObject
from selenium.webdriver.common.by import By
from config import URL

class ValueValidatePage(BaseObject):

    CHECK_VALIDATE_VALUE_PAGE = URL.CHECK_AND_VALIDATE_URL
    VALUE_FIELD = (By.ID, "dataInput")
    VALIDATION_SQUARE = (By.ID, "validationSquare")
    SELECT_BTN = (By.CLASS_NAME, "dropdown")
    VALIDATION_SECTION_BTN = (By.XPATH, "//a[@href='check_and_validate.html']")
    PROPERTY_NAME_COLOR = "background-color"
    BACK_BTN = (By.CLASS_NAME, "back-button")


    def __init__(self, driver):
        super().__init__(driver)

    def open_section(self):
        self.driver.get(self.CHECK_VALIDATE_VALUE_PAGE)

    def enter_value(self, value):
        self.send_keys(self.VALUE_FIELD, value)

    def get_message(self):
        return self.get_text(self.VALIDATION_SQUARE)

    def get_color(self):
        return self.get_css_property(self.VALIDATION_SQUARE, self.PROPERTY_NAME_COLOR)


