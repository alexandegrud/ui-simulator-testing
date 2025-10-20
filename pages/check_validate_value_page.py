from base.base import BaseObject
from selenium.webdriver.common.by import By
import allure

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

    @allure.step("Переход в раздел Check and Validate")
    def open_section(self):
        self.driver.get(self.url)

    @allure.step("Ввод значения")
    def enter_value(self, value):
        self.send_keys(self.VALUE_FIELD, value)

    @allure.step("Получение сообщения после ввода значения")
    def get_message(self):
        return self.get_text(self.VALIDATION_SQUARE)

    @allure.step("Получение цвета после ввода значения")
    def get_color(self):
        return self.get_css_property(self.VALIDATION_SQUARE, self.PROPERTY_NAME_COLOR)


