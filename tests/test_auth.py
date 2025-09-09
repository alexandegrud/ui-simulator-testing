from pytest import mark

def test_login(init_login_page):
    init_login_page.login()
    init_login_page.assertions.is_equal(
        expected="https://toghrulmirzayev.github.io/ui-simulator/hover_and_select.html",
        actual=init_login_page.get_current_url())

@mark.parametrize(
    "login, password, expected_error",
    [
        ("correct_username213", "correct_password", "Password or username is incorrect"),
        ("", "", "Username and password fields cannot be empty"),
        ("correct_username", "", "Password field cannot be empty"),
        ("", "correct_password", "Username field cannot be empty"),
    ],
    ids=[
        "Incorrect login or password",
        "Empty login and password",
        "Empty password field",
        "Empty login field",
    ]
)
def test_invalid_login(init_login_page, login, password, expected_error):
    init_login_page.login(login, password)
    init_login_page.assertions.is_equal(init_login_page.get_error_msg(), expected_error)

def test_logout(init_login_page):
    init_login_page.login()
    init_login_page.click_logout()
    init_login_page.assertions.is_equal(
        init_login_page.get_current_url(),
        "https://toghrulmirzayev.github.io/ui-simulator/index.html")
