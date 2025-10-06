from base.base import BaseObject
from selenium.webdriver.common.by import By

class SortingPage(BaseObject):

    NAME_SORTING_BTN = (By.XPATH, "//th[@onclick='sortTable(0)']")
    AGE_SORTING_BTN = (By.XPATH, "//th[@onclick='sortTable(1)']")
    ROLE_SORTING_BTN = (By.XPATH, "//th[@onclick='sortTable(2)']")
    ROWS_IN_TABLE = (By.XPATH, "//tbody//tr")


    def __init__(self, url, driver):
        self.name_sort_enabled = False
        self.age_sort_enabled = False
        self.role_sort_enabled = False
        self.url = url
        super().__init__(driver)

    def open_section(self):
        self.driver.get(self.url)

    def set_name_sort(self, on: bool):
        if self.name_sort_enabled != on:
            self.click(self.NAME_SORTING_BTN)
            self.name_sort_enabled = on

    def set_age_sort(self, on: bool):
        if self.age_sort_enabled != on:
            self.click(self.AGE_SORTING_BTN)
            self.age_sort_enabled = on

    def set_role_sort(self, on: bool):
        if self.role_sort_enabled != on:
            self.click(self.ROLE_SORTING_BTN)
            self.role_sort_enabled = on

    def get_text_from_rows(self):
        return self.get_texts_of_all_elements(self.ROWS_IN_TABLE)

    def get_column(self, get_name_column=False, get_age_column=False, get_role_column=False):
        texts = self.get_text_from_rows()
        column = []
        for text in texts:
            new_text = text.split()
            if get_name_column:
                column.append(new_text[0])
            elif get_age_column:
                column.append(new_text[1])
            elif get_role_column:
                column.append(new_text[2])
        return column




