import time
class Decorator:

    @staticmethod
    def retry(timeout, poll_frequency, exception, message=None):
        """
            Декоратор для повторных попыток выполнения функции.

            :param timeout: время ожидания в секундах
            :param poll_frequency: частота повторных вызовов
            :param exception: тип исключения, который будет поднят
            :param message: сообщение об ошибке
        """
        def decorator(func):
            def wrapper(*args, **kwargs):
                end_time = time.time() + timeout
                while time.time() < end_time:
                    result = func(*args, **kwargs)
                    if result:
                        return result
                    time.sleep(poll_frequency)
                err_msg = message or "Function '{func}' did not succeed within {timeout} seconds"
                raise exception(err_msg.format(func=func.__name__, timeout=timeout, poll_frequency=poll_frequency))
            return wrapper
        return decorator

    @staticmethod
    def delay(timeout, poll_frequency):
        def decorator(func):
            def wrapper(*args, **kwargs):
                end_time = time.time() + timeout
                while time.time() < end_time:
                    time.sleep(poll_frequency)
                return func(*args, **kwargs)
            return wrapper
        return decorator