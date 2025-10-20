from pytest import mark
from helper.digits_utils import DigitsUtils
import allure

@mark.parametrize(
    "max_number, attempts_count, expected_message",
    [
        (-1, -1, "Please enter valid configurations"),
        (1, "", "Please enter valid configurations"),
        ("", 1, "Please enter valid configurations"),
        (0, 0, "Please enter valid configurations"),
        ("", "", "Please enter valid configurations"),
    ],
    ids=[
        "Negative values",
        "Attempts field is empty",
        "Max number field is empty",
        "Only zeros",
        "All empty",
    ]
)

@allure.title("Проверка появление об ошибки при невалидных конфигурациях игры")
@allure.description("Проверка появление об ошибки при невалидных конфигурациях игры")
@allure.suite("Game page")
def test_invalid_config_game(init_game_page, max_number, attempts_count, expected_message):
    init_game_page.open_sections()
    init_game_page.enter_parameter_for_game_and_start(max_number, attempts_count)
    init_game_page.assertions.is_equal(
        init_game_page.get_text_of_config_error_message(),
        expected_message
    )

@mark.parametrize(
    "max_number, attempts_count, guess_value, expected_message",
    [
        (2, 2, -1, "Please enter a valid guess number"),
        (2, 2, "", "Please enter a valid guess number"),
    ],
    ids=[
        "Negative values",
        "Empty",
    ]
)

@allure.title("Проверка появление об ошибки при невалидном значении Guess")
@allure.description("Проверка появление об ошибки при невалидном значении Guess")
@allure.suite("Game page")
def test_invalid_guess_value(init_game_page, max_number, attempts_count, guess_value, expected_message):
    init_game_page.open_sections()
    init_game_page.enter_parameter_for_game_and_start(max_number, attempts_count)
    init_game_page.enter_guess_and_check(guess_value)
    init_game_page.assertions.is_equal(
        init_game_page.get_text_of_guess_error_message(),
        expected_message
    )

@mark.parametrize(
    "max_number, attempts_count",
    [
        (5, 6),
        (1, 1),
    ],
    ids=[
        "Regular value",
        "Minimum max value",
    ]
)

@allure.title("Значение Guess не превышает максимальное значение")
@allure.description("Значение Guess не превышает максимальное значение заданное при конфигурации игры")
@allure.suite("Game page")
def test_secret_number_less_or_equal_max(init_game_page, max_number, attempts_count):
    init_game_page.open_sections()
    init_game_page.enter_parameter_for_game_and_start(max_number, attempts_count)
    init_game_page.assertions.is_less_or_equal(
        init_game_page.guess_number(attempts_count),
        max_number
    )

@mark.parametrize(
    "max_number, attempts_count, guess_value, win, expected_message",
    [
        (1, 2, 0, True, "Congratulations! You guessed the secret number -> {secret_number}"),
        (1, 2, 2, False, "Try again! Guess lower"),
        (2, 2, 0, False, "Try again! Guess higher"),
        (1, 1, 7, False, "Game over! You ran out of attempts")
    ],
    ids=[
        "Win game",
        "Secret number lower",
        "Secret number higher",
        "Lose game",
    ]
)

@allure.title("Проверка сообщения о результате игры")
@allure.description("""Тест проверяет корректность отображения сообщения после попытки угадать число:
- Если число угадано 
- Если число больше/меньше
- Если закончились попытки
""")
@allure.suite("Game page")
def test_validate_result_message(init_game_page, max_number, attempts_count, guess_value, win, expected_message):
    init_game_page.open_sections()
    result_message = init_game_page.check_result_message(max_number, attempts_count, guess_value, win)
    secret_number = DigitsUtils.extract_digits(result_message)
    init_game_page.assertions.is_equal(
        result_message,
        expected_message.format(secret_number=secret_number)
    )

@mark.parametrize(
    "max_number, attempts_count, guess_value, win, lose, expected_message",
    [
        (2, 2, 10, False, True, "The secret number was {number_from_message}"),
        (3, 3, 4, False, False, "Attempts: 2/3"),
        (1, 4, 0, True, False, "It took you {number_from_message} attempts"),
    ],
    ids=[
        "Lose game",
        "Checking spent attempts",
        "Win game",
    ]
)

@allure.title("Проверка сообщения о попытках")
@allure.description("""Тест проверяет корректность отображения сообщения о попытках при окончании игры:
- Если число не угадано
- Если число угадано
- Если закончились попытки
""")
@allure.suite("Game page")
def test_validate_attempts_message(init_game_page, max_number, attempts_count, guess_value, win, lose, expected_message):
    init_game_page.open_sections()
    attempts_message = init_game_page.check_attempts_message(max_number, attempts_count, guess_value, win, lose)
    number_from_message = DigitsUtils.extract_digits(attempts_message)
    init_game_page.assertions.is_equal(
        attempts_message,
        expected_message.format(number_from_message=number_from_message)
    )

@allure.title("Проверка отображаемого количества попыток в rules")
@allure.description("Тест проверяет совпадает ли количество попыток заданных при конфигурации с количеством в rules")
@allure.suite("Game page")
def test_check_attempts_count_in_rules(init_game_page):
    max_number = 2
    attempts_count = 3
    init_game_page.open_sections()
    init_game_page.enter_parameter_for_game_and_start(max_number, attempts_count)
    init_game_page.assertions.is_equal(
        init_game_page.get_number_of_attempts_from_rules(),
        attempts_count
    )

@allure.title("Проверка корректности отображения значения Guess в сообщении о результате игры")
@allure.description("Отгадывается число guess и проверяется что оно совпадает с число из сообщения о результатах игры")
@allure.suite("Game page")
def test_check_secret_number_from_result_message(init_game_page):
    max_number = 2
    attempts_count = 3
    init_game_page.open_sections()
    init_game_page.enter_parameter_for_game_and_start(max_number, attempts_count)
    guess_number = init_game_page.guess_number(attempts_count)
    init_game_page.assertions.is_equal(
        init_game_page.get_guess_number_from_result_message(),
        guess_number
    )
