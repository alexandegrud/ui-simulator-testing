from pytest import mark
import time
@mark.parametrize(
    "value,expected_value",
    [
        (1, 1),
        (50, 50),
    ],
    ids=[
        "Minimum delay value",
        "Max delay value",
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
        ("", "Please enter a number between 1 and 50")
    ],
    ids=[
        "Above the max",
        "Under the min",
        "In range - value: 1",
        "In range - value: 50",
        "In range - value: 25",
        "Empty",
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


#Autocomlete

@mark.parametrize(
    "text",
    [
        "P",
        "C",
        "Swift",
        "Ru",
        "Ja",
    ],
    ids= [
        "A 1-letter search query",
        "A 1-letter search query",
        "Full-word search query",
        "A 2-letter search query",
        "A 2-letter search query",
    ]
)

def test_autocomplete_correctness(init_asynchronous_operation_page, text):
    init_asynchronous_operation_page.open_section()
    init_asynchronous_operation_page.autocomplete.enter_text(text)
    init_asynchronous_operation_page.assertions.is_contains_text(
        text,
        init_asynchronous_operation_page.autocomplete.get_text_from_autocomplete_list()
    )

@mark.parametrize(
    "text, expected_message",
    [
        ("1234", "Empty"),
        ("ыа", "Empty"),
        ("!@##%$", "Empty"),
        ("   ", "Empty"),
        ("", "Empty"),
    ],
    ids=[
        "Only digit",
        "Cyrillic letters",
        "Special characters",
        "Only spaces",
        "Empty",
    ]
)

def test_invalid_search(init_asynchronous_operation_page, text, expected_message):
    init_asynchronous_operation_page.open_section()
    init_asynchronous_operation_page.autocomplete.enter_text(text)
    init_asynchronous_operation_page.assertions.is_equal(
        init_asynchronous_operation_page.autocomplete.get_text_from_autocomplete_list(),
        expected_message
    )

#Infinite Scroll

@mark.parametrize(
    "stop_count, expected_count",
    [
        (50, 50),
        (100, 100),
    ],
    ids=[
        "50 items in list",
        "100 items in list",
    ]
)

def test_infinite_scrolling(init_asynchronous_operation_page, stop_count, expected_count):
    init_asynchronous_operation_page.open_section()
    init_asynchronous_operation_page.infinite_scroll.scroll_to_section()
    count = init_asynchronous_operation_page.infinite_scroll.scroll_and_get_items_list(stop_count=stop_count)
    init_asynchronous_operation_page.assertions.is_equal(
        count,
        expected_count
    )
    print(count)

# Error Handing

def test_check_error_simulated_msg(init_asynchronous_operation_page):
    expected_message = "An error occurred: Simulated error"
    init_asynchronous_operation_page.open_section()
    init_asynchronous_operation_page.error_handling.scroll_to_section()
    init_asynchronous_operation_page.error_handling.trigger_error()
    init_asynchronous_operation_page.assertions.is_equal(
        init_asynchronous_operation_page.error_handling.get_error_message(),
        expected_message
    )

def test_check_processing_msg(init_asynchronous_operation_page):
    expected_message = "Processing request..."
    init_asynchronous_operation_page.open_section()
    init_asynchronous_operation_page.error_handling.scroll_to_section()
    init_asynchronous_operation_page.error_handling.trigger_error()
    init_asynchronous_operation_page.assertions.is_equal(
        init_asynchronous_operation_page.error_handling.get_message(),
        expected_message
    )



