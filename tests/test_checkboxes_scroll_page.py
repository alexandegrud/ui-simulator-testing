from pytest import mark
import allure

@mark.parametrize(
    "count_checkbox_to_enable, checkboxes_to_disable, expected_checkbox_count",
    [
        (15, 15, "0"),
        (15, 0, "15"),
        (15, 14, "1"),
        (1, 0, "1"),
        (0, 0, "0"),
    ],
    ids=[
        "enable all and disable all",
        "enable all and disable 0",
        "enable all and disable 14",
        "enable 1 and disable 0",
        "enable 0 and disable 0",
    ]

)
@allure.title("Проверка корректности счетчика при включении/ыключении чекбоксов")
@allure.description("""Тест проверяет работу чекбоксов:
- Включается указанное количество чекбоксов
- Затем часть из них отключается
- Проверяется, что счётчик активных чекбоксов отображает правильное значение
""")
@allure.suite("Checkboxes and scroll")
def test_enable_and_disable_checkbox(init_checkbox_page, count_checkbox_to_enable,
                                     checkboxes_to_disable, expected_checkbox_count):
    init_checkbox_page.open_section()
    init_checkbox_page.enable_and_disable_checkbox(count_checkbox_to_enable, checkboxes_to_disable)
    init_checkbox_page.assertions.is_equal(
        init_checkbox_page.get_checkbox_counter(),
        expected_checkbox_count
    )