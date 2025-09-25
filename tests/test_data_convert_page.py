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

