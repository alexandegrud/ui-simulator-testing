from base.base import BaseObject
from selenium.webdriver.common.by import By
import json
import yaml

class DataConvertPage(BaseObject):

    CONVERT_TO_JSON_BTN = (By.ID, "toJson")
    CONVERT_TO_YAML_BTN = (By.ID, "toYaml")
    INPUT_DATA_FIELD = (By.ID, "inputData")
    OUTPUT_DATA_FIELD = (By.ID, "outputData")

    def __init__(self, url, driver):
        super().__init__(driver)
        self.url = url

    def open_section(self):
        self.driver.get(self.url)

    def convert_data_to_json(self):
        self.click(self.CONVERT_TO_JSON_BTN)

    def convert_data_to_yaml(self):
        self.click(self.CONVERT_TO_YAML_BTN)

    def input_json_data(self, data):
        data_json = json.dumps(data)
        self.send_keys(self.INPUT_DATA_FIELD, data_json)

    def input_yaml_data(self, data):
        data_yaml = yaml.dump(data)
        self.send_keys(self.INPUT_DATA_FIELD, data_yaml)

    def get_output_data(self):
        return self.get_input_or_output_text(self.OUTPUT_DATA_FIELD)

    def detect_format(self):
        data = self.get_output_data()
        data_strip = data.strip()
        if data_strip.startswith("{") or data_strip.endswith("["):
            return "The data has json format"
        else:
            return "The data has yaml format"

