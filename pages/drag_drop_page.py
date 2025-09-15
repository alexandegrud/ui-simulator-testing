from selenium.common import TimeoutException
from base.base import BaseObject
from selenium.webdriver.common.by import By
from config import URL
import time

class DragDropPage(BaseObject):

    DRAG_AND_DROP_URL = URL.DRAG_DROP_URL
    LETTERS_IN_CONTAINER = (By.CLASS_NAME, 'item')
    DONE_MESSAGE = (By.CLASS_NAME, 'done')


    def __init__(self, driver):
        super().__init__(driver)

    def open_section(self):
        self.driver.get(self.DRAG_AND_DROP_URL)

    def get_all_letters_in_container(self):
        return self.get_all_elements_located(self.LETTERS_IN_CONTAINER)

    def get_letters_container(self):
        letters = self.get_all_letters_in_container()
        return letters

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

    def get_text_of_success_message(self):
        try:
            return self.get_text(self.DONE_MESSAGE)
        except TimeoutException:
            return "The message was not displayed"

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

