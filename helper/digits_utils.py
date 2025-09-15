class DigitsUtils:

    @staticmethod
    def extract_digits(text):
        text = text.replace(" ", "")
        nums = ""
        for char in text:
            if char.isdigit():
                nums += char
        return int(nums) if nums else None