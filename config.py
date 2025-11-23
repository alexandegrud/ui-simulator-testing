from dotenv import load_dotenv
import os
from typing import Final

load_dotenv()


class URL:
    def __init__(self, env_config: str):
        self.BASE_URL: Final[str] = os.getenv("BASE_URL").format(env_config).lower()
        self.DRAG_DROP_URL: Final[str] = f"{self.BASE_URL}/drag-and-drop.html"
        self.INPUT_AND_CLICK_URL: Final[str] = f"{self.BASE_URL}/input-and-click.html"
        self.CHECKBOXES_AND_SCROLL_URL: Final[str] = f"{self.BASE_URL}/checkbox-and-scroll.html"
        self.CHECK_AND_VALIDATE_URL: Final[str] = f"{self.BASE_URL}/check_and_validate.html"
        self.SORTING_URL: Final[str] = f"{self.BASE_URL}/sorting.html"
        self.GAME_URL: Final[str] = f"{self.BASE_URL}/game.html"
        self.ASYNCHRONOUS_OPERATIONS_URL: Final[str] = f"{self.BASE_URL}/async_operations.html"
        self.DATA_CONVERTER_URL: Final[str] = f"{self.BASE_URL}/data_converter.html"

class Secrets:
    USER_NAME: Final[str] = os.getenv("USER_NAME")
    PASSWORD: Final[str] = os.getenv("PASSWORD")
    PAT_TOKEN: Final[str] = os.getenv("PAT_TOKEN")