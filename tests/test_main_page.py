
def test_open_all_sections(init_main_page):
    result = init_main_page.open_all_page_and_get_url()
    init_main_page.assertions.multiply_assertions(result, init_main_page.assertions.is_equal)

def test_turn_night_mode(init_main_page):
    expected_color = "rgba(51, 51, 51, 1)"
    init_main_page.turn_on_night_mode()
    init_main_page.assertions.is_equal(
        init_main_page.get_back_ground_color(),
        expected_color
    )