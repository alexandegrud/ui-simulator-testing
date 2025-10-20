from selenium.common import TimeoutException
from base.base import BaseObject
from selenium.webdriver.common.by import By
import time
import allure

class DragDropPage(BaseObject):

    LETTERS_IN_CONTAINER = (By.CLASS_NAME, 'item')
    DONE_MESSAGE = (By.CLASS_NAME, 'done')


    def __init__(self, url, driver):
        super().__init__(driver)
        self.url = url

    @allure.step("Переход в раздел Drag and drop")
    def open_section(self):
        self.driver.get(self.url)

    @allure.step("Получение всех букв")
    def get_letters_container(self):
        letters = self.get_all_elements_located(self.LETTERS_IN_CONTAINER)
        return letters

    @allure.step("Составление слова из букв")
    def construct_word(self, word_to_construct):
        letters = self.get_letters_container()

        letter_map = {}
        for letter in letters:
            letter_char = letter.text
            letter_map[letter] = letter_char

        for index, char in enumerate(word_to_construct):
            target_letter_element = letters[index]
            moving_letter_element = None
            for key, value in letter_map.items():
                if value == char:
                    moving_letter_element = key
                    del letter_map[key]
                    break

            if moving_letter_element != target_letter_element:
                self.drag_and_drop(moving_letter_element, target_letter_element)
                letters = self.get_letters_container()

    @allure.step("Получение текста из сообщения об успехе")
    def get_text_of_success_message(self):
        try:
            return self.get_text(self.DONE_MESSAGE)
        except TimeoutException:
            return "The message was not displayed"

    @allure.step("Проверка что кнопка мигает")
    def check_button_blinking(self, timeout=5, poll_frequency=1):
        end_time = time.time() + timeout
        while time.time() < end_time:
            try:
                background_color = self.get_css_property(self.DONE_MESSAGE, "background-color")
                time.sleep(poll_frequency)
                current_background_color = self.get_css_property(self.DONE_MESSAGE, "background-color")
                if current_background_color == background_color:
                    return "The button doesn't blinking"
            except TimeoutException:
                return "The button did not appear"
        return "The button is blinking"

