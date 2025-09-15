from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.asynchronous_operation_page import AsynchronousOperationPage
from pages.drag_drop_page import DragDropPage
from pages.game_page import GamePage
from pages.input_click_page import InputClickPage
from pages.login_page import LoginPage
from pages.check_validate_value_page import ValueValidatePage
from pages.checkboxes_scroll_page import CheckboxesScrollPage
from pages.main_page import MainPage



@fixture
def get_chrome_options():
    options = ChromeOptions()
    return options


@fixture
def get_webdriver(get_chrome_options):
    driver = webdriver.Chrome(options=get_chrome_options, service=Service(ChromeDriverManager().install()))
    return driver


@fixture
def setup(get_webdriver):
    url = 'https://toghrulmirzayev.github.io/ui-simulator/'
    get_webdriver.get(url)
    yield get_webdriver
    get_webdriver.quit()

@fixture
def init_login_page(setup):
    return LoginPage(driver=setup)

@fixture
def init_main_page(init_login_page, setup):
    init_login_page.login()
    return MainPage(driver=setup)

@fixture
def init_value_validate_page(init_login_page, setup):
    init_login_page.login()
    return ValueValidatePage(driver=setup)

@fixture
def init_input_click_page(init_login_page, setup):
    init_login_page.login()
    return InputClickPage(driver=setup)

@fixture
def init_checkbox_page(init_login_page, setup):
    init_login_page.login()
    return CheckboxesScrollPage(driver=setup)

@fixture
def init_asynchronous_operation_page(init_login_page, setup):
    init_login_page.login()
    return AsynchronousOperationPage(driver=setup)

@fixture
def init_drag_and_drop_page(init_login_page, setup):
    init_login_page.login()
    return DragDropPage(driver=setup)

@fixture
def init_game_page(init_login_page, setup):
    init_login_page.login()
    return GamePage(driver=setup)

