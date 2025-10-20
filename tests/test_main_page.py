import allure

@allure.title("Открываем все разделы")
@allure.description("Открываем все разделы и запоминаем актуальный url, затем сравниваем его с ожидаемым url")
@allure.suite("Main page")
def test_open_all_sections(init_main_page):
    result = init_main_page.open_all_page_and_get_url()
    init_main_page.assertions.multiply_assertions(result, init_main_page.assertions.is_equal)

@allure.title("Включаем night mode")
@allure.description("Включаем night mode и затем сравниваем актуальный цвет бэк-граунда с ожидаемым")
@allure.suite("Main page")
def test_turn_night_mode(init_main_page):
    expected_color = "rgba(51, 51, 51, 1)"
    init_main_page.turn_on_night_mode()
    init_main_page.assertions.is_equal(
        init_main_page.get_back_ground_color(),
        expected_color
    )