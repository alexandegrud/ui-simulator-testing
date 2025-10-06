from base.base import BaseObject
from selenium.webdriver.common.by import By

class MainPage(BaseObject):

    SELECT_BTN = (By.CLASS_NAME, 'dropdown')
    DRAG_AND_DROP_BTN = (By.XPATH, '//a[@href="drag-and-drop.html"]')
    INPUT_AND_CLICK_BTN = (By.XPATH, '//a[@href="input-and-click.html"]')
    CHECKBOXES_AND_SCROLL_BTN = (By.XPATH, '//a[@href="checkbox-and-scroll.html"]')
    CHECK_AND_VALIDATE_BTN = (By.XPATH, '//a[@href="check_and_validate.html"]')
    SORTING_BTN = (By.XPATH, '//a[@href="sorting.html"]')
    GAME_BTN = (By.XPATH, '//a[@href="game.html"]')
    ASYNC_OPERATION_BTN = (By.XPATH, '//a[@href="async_operations.html"]')
    DATA_CONVERTER_BTN = (By.XPATH, '//a[@href="data_converter.html"]')
    BACK_BTN = (By.CLASS_NAME, 'back-button')
    DAY_NIGHT_BTN = (By.CLASS_NAME, 'toggle-switch')
    MAIN_PAGE_BODY = (By.XPATH, "//body")



    def __init__(self, url, driver):
        super().__init__(driver)
        self.url = url

    def open_all_page_and_get_url(self):

        page_to_check = [
            ("DRAG_AND_DROP", self.DRAG_AND_DROP_BTN, self.url.DRAG_DROP_URL),
            ("INPUT_AND_CLICK", self.INPUT_AND_CLICK_BTN, self.url.INPUT_AND_CLICK_URL),
            ("CHECKBOXES_AND_SCROLL", self.CHECKBOXES_AND_SCROLL_BTN, self.url.CHECKBOXES_AND_SCROLL_URL),
            ("CHECK_AND_VALIDATE", self.CHECK_AND_VALIDATE_BTN, self.url.CHECK_AND_VALIDATE_URL),
            ("SORTING", self.SORTING_BTN, self.url.SORTING_URL),
            ("GAME", self.GAME_BTN, self.url.GAME_URL),
            ("ASYNC_OPERATION", self.ASYNC_OPERATION_BTN, self.url.ASYNCHRONOUS_OPERATIONS_URL),
            ("DATA_CONVERTER", self.DATA_CONVERTER_BTN, self.url.DATA_CONVERTER_URL),
        ]
        result = []
        for name, locator, expected_url in page_to_check:
            self.hover(self.SELECT_BTN)
            self.hover(locator)
            self.click(locator)
            actual_url = self.get_current_url()
            result.append((name, actual_url, expected_url))
            self.click(self.BACK_BTN)

        return result

    def turn_on_night_mode(self):
        self.click(self.DAY_NIGHT_BTN)

    def get_back_ground_color(self):
        return self.get_css_property(self.MAIN_PAGE_BODY, "background-color")