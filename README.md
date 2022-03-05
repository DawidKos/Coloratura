![Latest version](https://img.shields.io/pypi/v/coloratura?color=%23f6d155&label=version&style=flat-square)

# 🦜Coloratura

##### Awsome **cprint()** function to colored terminal text. Supported full RGB!

### Installation

You can install coloratura with **pip** as follows:

```
pip install coloratura
```

### Usage

First of all, get the basic cprint functions and selected color palettes:

```python
from coloratura import cprint, Pantone, Bit4
```

Printing colored text is incredibly ea``sy:

```python
cprint('This text is in the CLASSIC BLUE color from the Pantone palette', color=Pantone.CLASSIC_BLUE)
```

**Easy right?**
But what if you want to print text with a colored background?

```python
cprint('This is great!', color=Pantone.EMERALD, bg=Pantone.ULTIMATE_GRAY)
```

You can also add styles to the font:

```python
cprint('This string is italic and green', color=Bit4.GREEN, styles=['italic'])
```

You can mix multiple text styles

```python
cprint('This string is italic and bold',, styles = ['italic', 'bold'])```
```

### Colors and styles

#### List of all styles

> bold, italic, underline, strong-underline, crossed-out, framed

**Remember:** Styles can be mixed together by including them in the list of strings

### List of all colors from the pantone palette:
>![pantone](https://img.shields.io/badge/-VERY__PERI-6868ac?style=flat-square&label=2022)
>![pantone](https://img.shields.io/badge/-ILLUMINATING-f5df4d?style=flat-square&label=2021)
>![pantone](https://img.shields.io/badge/-ULTIMATE_GRAY-97999b?style=flat-square&label=2021)
>![pantone](https://img.shields.io/badge/-CLASSIC_BLUE-0f4c81?style=flat-square&label=2020)
>![pantone](https://img.shields.io/badge/-LIVING_CORAL-ff6f61?style=flat-square&label=2019)
>![pantone](https://img.shields.io/badge/-ULTRA_VIOLET-5f4b8b?style=flat-square&label=2018)
>![pantone](https://img.shields.io/badge/-GREENERY-88b04b?style=flat-square&label=2017)
>![pantone](https://img.shields.io/badge/-ROSE_QUARTZ-f7cac9?style=flat-square&label=2016)
>![pantone](https://img.shields.io/badge/-SERENITY-92a8d1?style=flat-square&label=2016)
>![pantone](https://img.shields.io/badge/-MARSALA-955251?style=flat-square&label=2015)
>![pantone](https://img.shields.io/badge/-RADIANT__ORCHID-b565a1?style=flat-square&label=2014)
>![pantone](https://img.shields.io/badge/-TURQUOISE-45b5aa?style=flat-square&label=2010)
>![pantone](https://img.shields.io/badge/-EMERALD-009b77?style=flat-square&label=2013)
>![pantone](https://img.shields.io/badge/-TANGERINE__TANGO-e34f33?style=flat-square&label=2012)
>![pantone](https://img.shields.io/badge/-HONEYSUCKLE-d85a7b?style=flat-square&label=2011)

### List of all colors from the 4bit palette

> BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, BRIGHT_BLACK, BRIGHT_RED, BRIGHT_GREEN, BRIGHT_YELLOW, BRIGHT_BLUE, BRIGHT_MAGENTA, BRIGHT_CYAN, BRIGHT_WHITE

**Too little? 🤔**

With the Color class you can define your own colors in the full RGB spectrum 🤯

Look how simple it is:

```python
YOUR_COLOR = Color('rgb', 191, 25, 50)
```

**Note:** Windows versions below Windows 10 do not support ANSI escape sequences so the colors will not be printed in
command prompt.

### *..and this is just the beginning of this great library!* 💚
