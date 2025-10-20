import allure
from pytest import mark

@allure.title("Конвертация данных в yaml формат")
@allure.description("Выполнение конвертации данных из json формата в yaml")
@allure.suite("Data convert page")
def test_convert_to_yaml(init_data_convert_page):
    data = {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }
    expected_message = "The data has yaml format"
    init_data_convert_page.open_section()
    init_data_convert_page.input_json_data(data)
    init_data_convert_page.convert_data_to_yaml()
    init_data_convert_page.assertions.is_equal(
        init_data_convert_page.detect_format(),
        expected_message
    )

@allure.title("Конвертация данных в json формат")
@allure.description("Выполнение конвертации данных из yaml формата в json")
@allure.suite("Data convert page")
def test_convert_to_json(init_data_convert_page):
    data = {
    "age": 30,
    "city": "New York",
    "name": "Alice",
    "skills": ["Python", "JavaScript"]
    }
    expected_message = "The data has json format"
    init_data_convert_page.open_section()
    init_data_convert_page.input_yaml_data(data)
    init_data_convert_page.convert_data_to_json()
    init_data_convert_page.assertions.is_equal(
        init_data_convert_page.detect_format(),
        expected_message
    )

