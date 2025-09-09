from dotenv import load_dotenv
import os
from typing import Final

load_dotenv()


class URL:

    BASE_URL: Final[str] = os.getenv("BASE_URL")
    DRAG_DROP_URL: Final[str] = f"{BASE_URL}/drag-and-drop.html"
    INPUT_AND_CLICK_URL: Final[str] = f"{BASE_URL}/input-and-click.html"
    CHECKBOXES_AND_SCROLL_URL: Final[str] = f"{BASE_URL}/checkbox-and-scroll.html"
    CHECK_AND_VALIDATE_URL: Final[str] = f"{BASE_URL}/check_and_validate.html"
    SORTING_URL: Final[str] = f"{BASE_URL}/sorting.html"
    GAME_URL: Final[str] = f"{BASE_URL}/game.html"
    ASYNCHRONOUS_OPERATIONS_URL: Final[str] = f"{BASE_URL}/async_operations.html"
    DATA_CONVERTER_URL: Final[str] = f"{BASE_URL}/data_converter.html"