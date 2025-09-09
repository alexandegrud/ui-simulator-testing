from pytest import mark

@mark.parametrize(
    "value, expected_message, expected_color",
    [
        (10, "Valid", "rgba(139, 195, 74, 1)"),
        (30, "Valid", "rgba(139, 195, 74, 1)"),
        (50, "Valid", "rgba(139, 195, 74, 1)"),
        (9, "Not in range", "rgba(244, 67, 54, 1)"),
        (51, "Not in range", "rgba(244, 67, 54, 1)"),
        (-11, "Negative integer", "rgba(244, 67, 54, 1)"),
        ("!@#", "Not a number", "rgba(244, 67, 54, 1)"),
        ("Dhb", "Not a number", "rgba(244, 67, 54, 1)"),
        ("Лом", "Not a number", "rgba(244, 67, 54, 1)"),
        ("54w", "Not a number", "rgba(244, 67, 54, 1)"),
    ],
    ids=[
        "In range (value = 10)",
        "In range (value = 30)",
        "In range (value = 50)",
        "Not in range (value = 9)",
        "Not in range (value = 51)",
        "Negative integer (value = -11)",
        "Not a number (value = !@#)",
        "Not a number (value = Dhb)",
        "Not a number (value = Лом)",
        "Not a number (value = 54w)",
    ]
)
def test_validate_value(init_value_validate_page, value, expected_message, expected_color):
    init_value_validate_page.open_section()
    init_value_validate_page.enter_value(value)
    init_value_validate_page.get_message()
    init_value_validate_page.get_color()
    init_value_validate_page.assertions.is_equal(init_value_validate_page.get_message(), expected_message)
    init_value_validate_page.assertions.is_equal(init_value_validate_page.get_color(), expected_color)

