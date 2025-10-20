from base.base import BaseObject
from selenium.webdriver.common.by import By
import allure

class InputClickPage(BaseObject):

    SELECT_BTN = (By.CLASS_NAME, 'dropdown')
    SECTION_BTN = (By.XPATH, '//a[@href="input-and-click.html"]')
    VALUE_FIELD = (By.ID, 'inputText')
    ADD_BTN = (By.ID, 'addBtn')
    DELETE_BTN = (By.ID, 'deleteBtn')
    BACK_BTN = (By.CLASS_NAME, 'back-button')
    ITEM_IN_CONTAINER = (By.CLASS_NAME, 'item')

    def __init__(self, url, driver):
        super().__init__(driver)
        self.url = url

    @allure.step("Переход в раздел 'Input and click'")
    def open_section(self):
        self.driver.get(self.url)

    def _enter_value(self, value):
        self.send_keys(self.VALUE_FIELD, value)

    def __add_value(self, value):
        self._enter_value(value)
        self.click(self.ADD_BTN)

    @allure.step("Добавление значений")
    def add_values(self, values):
        for value in values:
            self.__add_value(value)

    @allure.step("Удаление значений")
    def delete_values(self, delete_count):
        i = 0
        while i < delete_count:
            self.click(self.DELETE_BTN)
            i += 1

    @allure.step("Получение всех текущих значений")
    def get_text_all_added_values(self):
        return self.get_texts_of_all_elements(self.ITEM_IN_CONTAINER)



