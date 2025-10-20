from selenium.common import TimeoutException
from base.base import BaseObject
from selenium.webdriver.common.by import By
from helper.decorators import Decorator
from helper.digits_utils import DigitsUtils
import allure

class AsynchronousOperationPage(BaseObject):


    def __init__(self, url, driver):
        super().__init__(driver)
        self.data_loading = DataLoading(self.driver)
        self.autocomplete = AutoComplete(self.driver)
        self.infinite_scroll = InfiniteScroll(self.driver)
        self.error_handling = ErrorHandling(self.driver)
        self.url = url

    @allure.step("Открытие раздела Asynchronous Operation")
    def open_section(self):
        self.driver.get(self.url)


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

    @allure.step("Удаление значения из поля")
    def clear_input_field(self):
        self.clear_backspace(self.INPUT_FIELD)

    @allure.step("Ввод значения")
    def enter_value(self, value):
        self.send_keys(self.INPUT_FIELD, value)

    @allure.step("Ввод значения и запуск")
    def enter_value_and_click(self, value):
        self.enter_value(value)
        self.click(self.LOAD_DATA_BTN)

    @Decorator.retry(50, 1, TimeoutException)
    @allure.step("Проверка окончания загрузки")
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

    @allure.step("Получение времени загрузки")
    def get_time_of_loaded(self):
        text = self.get_text(self.TEXT_FIELD)
        return DigitsUtils.extract_digits(text)

    @allure.step("Наведение курсора на кнопку Load")
    def hover_to_load_btn(self):
        self.hover(self.ERROR_MESSAGE)

    @allure.step("Проверка что кнопка некликабельна")
    def check_load_btn_is_not_clickable(self):
        return self.is_not_clickable(self.LOAD_DATA_BTN, timeout=2)

    @allure.step("Получение текста из сообщения об ошибки")
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    @allure.step("Получение цвета кнопки")
    def get_color_of_load_btn(self):
        return self.get_css_property(self.LOAD_DATA_BTN, self.PROPERTY_NAME_COLOR_OF_LOAD_BTN)

    @allure.step("Проверка отображения галочки")
    def check_checkmark_is_displayed(self):
        try:
            return self._get_visible(self.CHECKMARK, timeout=4)
        except TimeoutException:
            raise TimeoutException("Checkmark did not appear")

    @allure.step("Проверка отображения индикатора загрузки")
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

    @allure.step("Ввод текста")
    def enter_text(self, text):
        self.send_keys(self.TEXT_FIELD, text)

    @allure.step("Получение текста из результата поиска")
    def get_text_from_autocomplete_list(self):
        list_of_text = self.get_texts_of_all_elements(self.AUTOCOMPLETE_ITEMS_LIST, timeout=2)
        return list_of_text or "Empty"

class InfiniteScroll(BaseObject):

    ITEMS_LIST = (By.ID, "infiniteScrollList")
    ITEM_IN_LIST = (By.XPATH, "//ul//li")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Скролл к секции Infinite Scroll")
    def scroll_to_section(self):
        self.scroll_to_element(self.ITEM_IN_LIST)

    @Decorator.delay(2, 1)
    @allure.step("Скролл списка и получение всех подгрузившихся объектов ")
    def scroll_and_get_items_list(self, stop_count=10):
        """
        Добавил декоратор delay, т к после скролла к разделу, сам раздел не успевал полностью подгрузиться и из-за этого
        число возвращаемое число items было меньше, чем на самом деле.

        """
        last_count = 0

        while True:
            current_count = self.get_items_count_in_list()

            if current_count >= stop_count or current_count == last_count:
                break
            else:
                self.scroll_element_by_step(self.ITEMS_LIST, 500)
                last_count = current_count
        return current_count


    def get_items_count_in_list(self):
        items = self.get_all_elements_located(self.ITEM_IN_LIST, timeout=2)
        return len(items)


class ErrorHandling(BaseObject):

    TRIGGER_ERROR_BTN = (By.ID, "errorBtn")
    ERROR_MESSAGE = (By.ID, "errorMessage")


    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Скролл к секции Error Handling")
    def scroll_to_section(self):
        self.scroll_to_element(self.ERROR_MESSAGE)

    @allure.step("Запуск появления ошибки")
    def trigger_error(self):
        self.click(self.TRIGGER_ERROR_BTN)

    def get_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    @Decorator.retry(10, 1, TimeoutException)
    @allure.step("Получения текста ошибки")
    def get_error_message(self):
        message = self.get_message()
        if message == "An error occurred: Simulated error":
            return message
        else:
            return False




