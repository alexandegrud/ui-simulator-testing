from selenium.webdriver.common.by import By
from config import URL
from base.base import BaseObject
from helper.digits_utils import DigitsUtils

class GamePage(BaseObject):

    GAME_PAGE_URL = URL.GAME_URL
    NUMBER_FIELD = (By.ID, 'maxNumber')
    ATTEMPTS_FIELD = (By.ID, 'maxAttempts')
    START_GAME_BTN = (By.ID, 'startBtn')
    ERROR_CONFIG_MSG = (By.ID, 'errorConfigMessage')
    GUESS_FILED = (By.ID, 'guess')
    CHECK_GUESS_BTN = (By.ID, 'playBtn')
    BACK_TO_CONFIG_BTN = (By.ID, 'backConfigBtn')
    RULES_TEXT = (By.XPATH, "//h3")
    ERROR_MSG = (By.ID, 'errorMessage')
    RESULT_MSG = (By.ID, 'resultMessage')
    ATTEMPTS_MSG = (By.ID, 'attemptsMessage')

    def __init__(self, driver):
        super().__init__(driver)

    def open_sections(self):
        self.driver.get(self.GAME_PAGE_URL)

    def get_text_of_config_error_message(self):
        return self.get_text(self.ERROR_CONFIG_MSG)

    def enter_parameter_for_game_and_start(self, max_number, attempts_count):
        self.send_keys(self.NUMBER_FIELD, max_number)
        self.send_keys(self.ATTEMPTS_FIELD, attempts_count)
        self.click(self.START_GAME_BTN)

    def get_text_of_guess_error_message(self):
        return self.get_text(self.ERROR_MSG)

    def enter_guess_and_check(self, value):
        self.send_keys(self.GUESS_FILED, value)
        self.click(self.CHECK_GUESS_BTN)

    def get_number_of_attempts_from_rules(self):
        text = self.get_text(self.RULES_TEXT)
        return DigitsUtils.extract_digits(text)

    def back_to_config(self):
        self.click(self.BACK_TO_CONFIG_BTN)

    def get_text_result_message(self):
        return self.get_text(self.RESULT_MSG)

    def get_guess_number_from_result_message(self):
        text = self.get_text(self.RESULT_MSG)
        return DigitsUtils.extract_digits(text)

    def guess_number(self, attempts_count):
        i = 0
        while i < attempts_count:
            self.enter_guess_and_check(i)
            result_text = self.get_text_result_message()
            if result_text == f"Congratulations! You guessed the secret number -> {i}":
                break
            self.clear(self.GUESS_FILED)
            i += 1
        return i

    def check_result_message(self, max_number, attempts_count, gues_value, win=False):
        if win:
            self.enter_parameter_for_game_and_start(max_number, attempts_count)
            self.guess_number(attempts_count)
            result_text = self.get_text_result_message()
            return result_text

        else:
            while True:
                self.enter_parameter_for_game_and_start(max_number, attempts_count)
                self.enter_guess_and_check(gues_value)
                text = self.get_text(self.RESULT_MSG)
                if "Congratulations" not in text:
                    return text
                self.back_to_config()

    def check_attempts_msg(self, max_number, attempts_count, gues_value, win=False, lose=False):
        self.enter_parameter_for_game_and_start(max_number, attempts_count)
        if lose:
            i = 0
            while i < attempts_count:
                self.clear(self.GUESS_FILED)
                self.enter_guess_and_check(gues_value)
                i += 1
            return self.get_text(self.ATTEMPTS_MSG)
        elif win:
            self.guess_number(attempts_count)
            return self.get_text(self.ATTEMPTS_MSG)
        else:
            i = 1
            while i < attempts_count:
                self.clear(self.GUESS_FILED)
                self.enter_guess_and_check(gues_value)
                i += 1

            return self.get_text(self.ATTEMPTS_MSG)
