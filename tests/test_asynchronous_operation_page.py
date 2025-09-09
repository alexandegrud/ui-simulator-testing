from pytest import mark
@mark.parametrize(
    "value,expected_value",
    [
        (1, 1),
        (50, 50),
    ]
)

def test_check_time_load(init_asynchronous_operation_page, value, expected_value):
    init_asynchronous_operation_page.open_section()
    init_asynchronous_operation_page.data_loading.clear_input_field()
    init_asynchronous_operation_page.data_loading.enter_value_and_click(value)
    init_asynchronous_operation_page.data_loading.is_loading_complete()
    init_asynchronous_operation_page.assertions.is_less_or_equal(
        init_asynchronous_operation_page.data_loading.get_time_of_loaded(),
        expected_value
    )

@mark.parametrize(
    "value, expected_message",
    [
        (51, "Please enter a number between 1 and 50"),
        (0, "Please enter a number between 1 and 50"),
        (1, ""),
        (50, ""),
        (25, ""),
        ("", "")
    ]
)

def test_invalid_value(init_asynchronous_operation_page, value, expected_message):
    init_asynchronous_operation_page.open_section()
    init_asynchronous_operation_page.data_loading.clear_input_field()
    init_asynchronous_operation_page.data_loading.enter_value(value)
    init_asynchronous_operation_page.assertions.is_equal(
        init_asynchronous_operation_page.data_loading.get_error_message(),
        expected_message
    )

def test_hover_state_of_load_button(init_asynchronous_operation_page):
    expected_color = "rgba(255, 193, 7, 1)"
    init_asynchronous_operation_page.open_section()
    init_asynchronous_operation_page.data_loading.hover_to_load_btn()
    init_asynchronous_operation_page.assertions.is_equal(
        init_asynchronous_operation_page.data_loading.get_color_of_load_btn(),
        expected_color
    )

def test_load_btn_is_not_clickable(init_asynchronous_operation_page):
    value = 100
    init_asynchronous_operation_page.open_section()
    init_asynchronous_operation_page.data_loading.clear_input_field()
    init_asynchronous_operation_page.data_loading.enter_value(value)
    init_asynchronous_operation_page.data_loading.check_load_btn_is_not_clickable()

def test_checkmark_is_displayed(init_asynchronous_operation_page):
    value = 2
    init_asynchronous_operation_page.open_section()
    init_asynchronous_operation_page.data_loading.clear_input_field()
    init_asynchronous_operation_page.data_loading.enter_value_and_click(value)
    init_asynchronous_operation_page.data_loading.check_checkmark_is_displayed()

def test_loading_indicator_is_displayed(init_asynchronous_operation_page):
    value = 5
    init_asynchronous_operation_page.open_section()
    init_asynchronous_operation_page.data_loading.clear_input_field()
    init_asynchronous_operation_page.data_loading.enter_value_and_click(value)
    init_asynchronous_operation_page.data_loading.check_loading_indicator_is_displayed()