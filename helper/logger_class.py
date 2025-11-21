import functools
import logging
import os
from dotenv import load_dotenv

load_dotenv()

LOGGER_CONFIG = int(os.getenv("LOGGER_CONFIG", 0))

logger = logging.getLogger("BaseLogger")
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(message)s')
logger.handlers = []

if LOGGER_CONFIG == 1:
    log_dir = "runtime"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "app.log")
    file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
elif LOGGER_CONFIG == 2:
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
elif LOGGER_CONFIG == 0:
    print("[BaseLogger] Logging disabled (LOGGER_CONFIG=0)")

# 🔑 list of sensitive keys to mask in logs
SENSITIVE_KEYS = {"password", "pwd", "secret", "token", "value"}


def sanitize_kwargs(kwargs: dict) -> dict:
    """Return a copy of kwargs with sensitive values masked."""
    return {k: ("***" if k.lower() in SENSITIVE_KEYS else v) for k, v in kwargs.items()}


def log_method(custom_message: str = ""):
    """
    Logger decorator for class methods or normal functions.
    Can be used as @log_method() or @log_method("message").
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if LOGGER_CONFIG == 0:
                return func(*args, **kwargs)

            func_name = func.name
            safe_kwargs = sanitize_kwargs(kwargs)
            params = f"args={args}, kwargs={safe_kwargs}"
            doc = func.doc or ""
            output = None

            try:
                result = func(*args, **kwargs)
                output = repr(result)
            except Exception as e:
                output = f"Exception: {e}"
                raise
            finally:
                log_message = (
                    f"\nFUNCTION: {func_name}\n"
                    f"PARAMS: {params}\n"
                    f"OUTPUT: {output}\n"
                    f"CUSTOM_MSG: {custom_message}\n"
                    f"DOC: {doc}\n"
                    "---------------------------"
                )
                logger.info(log_message)
            return result
        return wrapper
    return decorator


def log_event(message: str, **kwargs):
    """
    Ad-hoc logging function, can be used anywhere without decorating a function.
    Automatically masks sensitive keys.
    """
    if LOGGER_CONFIG == 0:
        return

    safe_kwargs = sanitize_kwargs(kwargs)
    log_message = (
        f"\nCUSTOM_LOG\nPARAMS: {safe_kwargs}\nMESSAGE: "
        f"{message}\n---------------------------"
    )
    logger.info(log_message)


class LoggingMeta(type):
    """
    Metaclass that applies the log_method decorator to all methods of a class.
    """
    def new(cls, name, bases, dct):
        for attr_name, attr_value in dct.items():
            if callable(attr_value) and not attr_name.startswith("__"):
                dct[attr_name] = log_method()(attr_value)
        return super().new(cls, name, bases, dct)