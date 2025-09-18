from selenium.common import TimeoutException
from base.base import BaseObject
from selenium.webdriver.common.by import By
from config import URL
from helper.decorators import Decorator
from helper.digits_utils import DigitsUtils

class AsynchronousOperationPage(BaseObject):

    ASYNCHRONOUS_OPERATION_PAGE_URL = URL.ASYNCHRONOUS_OPERATIONS_URL

    def __init__(self, driver):
        super().__init__(driver)
        self.data_loading = DataLoading(self.driver)
        self.autocomplete = AutoComplete(self.driver)

    def open_section(self):
        self.driver.get(self.ASYNCHRONOUS_OPERATION_PAGE_URL)


class DataLoading(BaseObject):

    INPUT_FIELD = (By.ID, 'loadingDelay')
    LOAD_DATA_BTN = (By.ID, 'loadDataBtn')
    PROPERTY_NAME_COLOR_OF_LOAD_BTN = "background-color"
    TEXT_FIELD = (By.ID, 'loadedData')
    ERROR_MESSAGE = (By.ID, 'delayError')
    CHECKMARK = (By.ID, 'checkIcon')
    LOADING_INDICATOR = (By.ID, 'loadingIndicator')

    def __init__(self, driver):
        super().__init__(driver)

    def clear_input_field(self):
        self.clear_backspace(self.INPUT_FIELD)

    def enter_value(self, value):
        self.send_keys(self.INPUT_FIELD, value)

    def enter_value_and_click(self, value):
        self.enter_value(value)
        self.click(self.LOAD_DATA_BTN)

    @Decorator.retry(50, 1, TimeoutException)
    def is_loading_complete(self):
        """
        Проверяет или завершилась загрузка.
        Возвращает True, если индикатор загрузки не отображается,
        и False, если он все еще видим.

        Retry - декоратор используемый для проверки видимости индикатора раз в секунду.
        """
        try:
            self._get_visible(self.LOADING_INDICATOR, timeout=1)
        except TimeoutException:
            return True

    def get_time_of_loaded(self):
        text = self.get_text(self.TEXT_FIELD)
        return DigitsUtils.extract_digits(text)

    def hover_to_load_btn(self):
        self.hover(self.ERROR_MESSAGE)

    def check_load_btn_is_not_clickable(self):
        return self.is_not_clickable(self.LOAD_DATA_BTN, timeout=2)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def get_color_of_load_btn(self):
        return self.get_css_property(self.LOAD_DATA_BTN, self.PROPERTY_NAME_COLOR_OF_LOAD_BTN)

    def check_checkmark_is_displayed(self):
        try:
            return self._get_visible(self.CHECKMARK, timeout=4)
        except TimeoutException:
            raise TimeoutException("Checkmark did not appear")

    def check_loading_indicator_is_displayed(self):
        try:
            return self._get_visible(self.LOADING_INDICATOR, timeout=2)
        except TimeoutException:
            raise TimeoutException("Loading indicator did not appear")


class AutoComplete(BaseObject):

    TEXT_FIELD = (By.ID, 'autocompleteInput')
    AUTOCOMPLETE_ITEMS_LIST = (By.XPATH, "//ul[@id='autocompleteList']//li")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_text(self, text):
        self.send_keys(self.TEXT_FIELD, text)

    def get_text_from_autocomplete_list(self):
        list_of_text = self.get_texts_of_all_elements(self.AUTOCOMPLETE_ITEMS_LIST, timeout=2)
        return list_of_text or "Empty"



