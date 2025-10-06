from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.asynchronous_operation_page import AsynchronousOperationPage
from pages.data_convert_page import DataConvertPage
from pages.drag_drop_page import DragDropPage
from pages.game_page import GamePage
from pages.input_click_page import InputClickPage
from pages.login_page import LoginPage
from pages.check_validate_value_page import ValueValidatePage
from pages.checkboxes_scroll_page import CheckboxesScrollPage
from pages.main_page import MainPage
from pages.sorting_page import SortingPage
from config import URL


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="io",
        help="Select environment"
    )

@fixture(scope="session")
def init_config(request):
    env_name = request.config.getoption("--env")
    config = URL(env_name)
    return config


@fixture
def get_chrome_options():
    options = ChromeOptions()
    return options


@fixture
def get_webdriver(get_chrome_options):
    driver = webdriver.Chrome(options=get_chrome_options, service=Service(ChromeDriverManager().install()))
    return driver


@fixture
def setup(get_webdriver, init_config):
    url = init_config.BASE_URL
    get_webdriver.get(url)
    yield get_webdriver
    get_webdriver.quit()

@fixture
def init_login_page(setup):
    return LoginPage(driver=setup)

@fixture
def init_main_page(init_login_page, setup, init_config):
    init_login_page.login()
    return MainPage(init_config, driver=setup)

@fixture
def init_value_validate_page(init_login_page, setup, init_config):
    init_login_page.login()
    return ValueValidatePage(init_config.CHECK_AND_VALIDATE_URL, driver=setup)

@fixture
def init_input_click_page(init_login_page, setup, init_config):
    init_login_page.login()
    return InputClickPage(init_config.INPUT_AND_CLICK_URL, driver=setup)

@fixture
def init_checkbox_page(init_login_page, setup, init_config):
    init_login_page.login()
    return CheckboxesScrollPage(init_config.CHECKBOXES_AND_SCROLL_URL, driver=setup)

@fixture
def init_asynchronous_operation_page(init_login_page, setup, init_config):
    init_login_page.login()
    return AsynchronousOperationPage(init_config.ASYNCHRONOUS_OPERATIONS_URL, driver=setup)

@fixture
def init_drag_and_drop_page(init_login_page, setup, init_config):
    init_login_page.login()
    return DragDropPage(init_config.DRAG_DROP_URL, driver=setup)

@fixture
def init_game_page(init_login_page, setup, init_config):
    init_login_page.login()
    return GamePage(init_config.GAME_URL, driver=setup)

@fixture
def init_sorting_page(init_login_page, setup, init_config):
    init_login_page.login()
    return SortingPage(init_config.SORTING_URL, driver=setup)

@fixture
def init_data_convert_page(init_login_page, setup, init_config):
    init_login_page.login()
    return DataConvertPage(init_config.DATA_CONVERTER_URL, driver=setup)

