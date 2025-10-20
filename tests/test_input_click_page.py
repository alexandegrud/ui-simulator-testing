from pytest import mark
import allure

@mark.parametrize(
    "values",
    [
        ["test1", "test2", "test3"],
        ["12312", "554", "232"],
        ["#$^@", "%^$&@", "////"],
        []
    ],
    ids=[
        "letters and nums",
        "only nums",
        "special symbol",
        "empty"
    ]
)
@allure.title("Добавление значений")
@allure.description("Добавление разных значений и проверка, что они добавились")
@allure.suite("Input and click page")
def test_add_value(init_input_click_page,values):
    init_input_click_page.open_section()
    init_input_click_page.add_values(values)
    init_input_click_page.assertions.is_equal(
        init_input_click_page.get_text_all_added_values(),
        values
    )

@mark.parametrize(
    "values, count_delete, values_expected",
    [
        (["123", "45", "67"], 1, ["123", "45"]),
        (["fsf", "!!!!", "67"], 2, ["fsf"]),
        (["dfsd", "232", "#$%$^"], 3, [])

    ],
    ids=[
        "delete 1 values",
        "delete 2 values",
        "delete all values",
    ]
)
@allure.title("Удаление значений")
@allure.description("Добавляем значение и затем удаляем необходимое количество, проверяем что значение удалились")
@allure.suite("Input and click page")
def test_delete_value(init_input_click_page, values, count_delete, values_expected):
    init_input_click_page.open_section()
    init_input_click_page.add_values(values)
    init_input_click_page.delete_values(count_delete)
    init_input_click_page.assertions.is_equal(
        init_input_click_page.get_text_all_added_values(),
        values_expected
    )
