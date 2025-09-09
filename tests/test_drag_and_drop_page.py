from pytest import mark

@mark.parametrize(
    "constructed_word, expected_message",
    [
        ("TESTING", "DONE"),
        ("ETSTING", "The message was not displayed"),
    ],
    ids=[
        "Correct word",
        "Incorrect word",
    ]
)
def test_construct_correct_word(init_drag_and_drop_page, constructed_word, expected_message):
    init_drag_and_drop_page.open_section()
    init_drag_and_drop_page.construct_word(constructed_word)
    init_drag_and_drop_page.assertions.is_equal(
        init_drag_and_drop_page.get_text_of_success_message(),
        expected_message
    )
@mark.parametrize(
    "constructed_word, expected_message",
    [
        ("TESTING", "The button is blinking"),
        ("ETSTING", "The button did not appear"),
    ],
    ids= [
        "Correct word, button is blinking",
        "Incorrect word, button does not appear",
    ]
)
def test_message_button_blinking(init_drag_and_drop_page, constructed_word, expected_message):
    init_drag_and_drop_page.open_section()
    init_drag_and_drop_page.construct_word(constructed_word)
    init_drag_and_drop_page.assertions.is_equal(
        init_drag_and_drop_page.check_button_blinking(),
        expected_message
    )
