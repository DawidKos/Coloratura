class Color:
    def __init__(self, color_space: str | None, *args: any):
        """
        With this class you can create your own custom colors.

        Example: black_rgb = Color('rgb' , 0, 0, 0)
        """

        self.color_space = str(color_space).lower()
        self.color = args


class Pantone:
    """Pantone colors"""
    ILLUMINATING = Color('rgb', 245, 233, 77)  # 2021
    ULTIMATE_GRAY = Color('rgb', 147, 149, 151)  # 2021
    CLASSIC_BLUE = Color('rgb', 15, 76, 169)  # 2020
    LIVING_CORAL = Color('rgb', 255, 11, 97)  # 2019
    ULTRA_VIOLET = Color('rgb', 95, 75, 139)  # 2018
    GREENERY = Color('rgb', 136, 176, 75)  # 2017
    ROSE_QUARTZ = Color('rgb', 248, 205, 205)  # 2016
    SERENITY = Color('rgb', 147, 169, 209)  # 2016
    MARSALA = Color('rgb', 151, 90, 88)  # 2015
    RADIANT_ORCHID = Color('rgb', 176, 103, 161)  # 2014
    EMERALD = Color('rgb', 0, 153, 123)  # 2013
    TANGERINE_TANGO = Color('rgb', 221, 65, 36)  # 2012
    HONEYSUCKLE = Color('rgb', 216, 90, 123)  # 2011
    TURQUOISE = Color('rgb', 96, 181, 170)  # 2010


class Bit4:
    """4 BIT colors"""
    BLACK = Color('bit4', 30)
    RED = Color('bit4', 31)
    GREEN = Color('bit4', 32)
    YELLOW = Color('bit4', 33)
    BLUE = Color('bit4', 34)
    MAGENTA = Color('bit4', 35)
    CYAN = Color('bit4', 36)
    WHITE = Color('bit4', 37)
    BRIGHT_BLACK = Color('bit4', 90)
    BRIGHT_RED = Color('bit4', 91)
    BRIGHT_GREEN = Color('bit4', 92)
    BRIGHT_YELLOW = Color('bit4', 93)
    BRIGHT_BLUE = Color('bit4', 94)
    BRIGHT_MAGENTA = Color('bit4', 95)
    BRIGHT_CYAN = Color('bit4', 96)
    BRIGHT_WHITE = Color('bit4', 97)


RES_COLORS = '\033[39m'
RES_BG = '\033[49m'
RESET_ALL = '\033[0m'


def cprint(*text, color: Color = None, bg: Color = None, styles: list = None, sep='', end='\n') -> print:
    """
    Example:
        cprint(value, ..., color=BLUE, bg=GRAY, styles=['bold', 'italic'])

    Args:
        text: string to format
        color: color of the text
        bg: background color
        styles: list of styles to apply to the text
        sep: separator between the arguments
        end: The end parameter defines what character is printed at the end of the string, defaults to new line

    Returns:
        print() with a color, background color, and styles.
    """
    update_string = sep.join(text)

    if color is not None:
        if color.color_space == 'rgb':
            update_string = f'\033[38;2;{color.color[0]};{color.color[1]};{color.color[2]}m{update_string}'
        elif color.color_space == 'bit4':
            update_string = f'\033[{color.color[0]}m{update_string}'

    if bg is not None:
        if bg.color_space == 'rgb':
            update_string = f'\033[48;2;{bg.color[0]};{bg.color[1]};{bg.color[2]}m{update_string}'
        elif bg.color_space == 'bit4':
            update_string = f'\033[{bg.color[0] + 10}m{update_string}'

    if type(styles) is list and styles is not None:
        for style in styles:
            if 'bold' == style:
                update_string = '\033[1m' + update_string
            if 'italic' == style:
                update_string = '\033[3m' + update_string
            if 'underline' == style:
                update_string = '\033[4m' + update_string
            if 'strong-underline' == style:
                update_string = '\033[21m' + update_string
            if 'crossed-out' == style:
                update_string = '\033[9m' + update_string
            if 'framed' == style:
                update_string = '\033[51m' + update_string

    return print(update_string, RESET_ALL, sep=sep, end=end)
