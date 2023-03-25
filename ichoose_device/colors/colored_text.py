class ColoredText:
    def __init__(self, text: str, color_code: str):
        self.__text = text
        self.__red = str(int(color_code[1:3], 16))
        self.__green = str(int(color_code[3:5], 16))
        self.__blue = str(int(color_code[5:7], 16))

    def __str__(self) -> str:
        return f"\x1b[38;2;{self.__red};{self.__green};{self.__blue}m{self.__text}\x1b[0m"
