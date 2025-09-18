class Assertions:

    @staticmethod
    def is_equal(actual, expected):
        assert actual == expected, f"Expected {expected}, but got {actual}"


    @staticmethod
    def is_not_equal(actual, expected):
        assert actual != expected, f"Expected {expected} to be not equal to {actual}, but they are equal"

    @staticmethod
    def multiply_assertions(result: list[tuple[str, str, str]], target_operation: callable):
        failed_list = []
        for name, actual, expected in result:
            try:
                target_operation(actual, expected)
            except AssertionError:
                failed_list.append((name, actual, expected))

        if failed_list:
            message = "\n".join(f"{name}: actual is {actual}, but expected {expected}"
                                for name, actual, expected in failed_list)
            raise AssertionError(f"Failed: {message}")

    @staticmethod
    def is_less_or_equal(actual, max_value):
            assert actual <= max_value, f"Actual {actual} more than {max_value}, but should be less or equal"

    @staticmethod
    def is_contains_text(text, source_texts : list):
        for source_text in source_texts:
            assert text.lower() in source_text.lower(), f"'{text}' not found in: '{source_texts}'"

    @staticmethod
    def are_digits_sorted(nums: list[int]):
        assert nums == sorted(nums), "The digits are not sorted"

    @staticmethod
    def is_text_sorted(texts: list):
        text_lower = [text.lower() for text in texts]
        assert text_lower == sorted(text_lower), "The text is not sorted"
