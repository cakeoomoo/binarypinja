#!/usr/bin/python3

from __future__ import print_function
from functools import partial


def print_noLF(text):
    print('%s' % (text), end='')


def print_colored(code, text, is_bold=False):
    if is_bold:
        code = '1;%s' % code
    print('\033[%sm%s\033[0m' % (code, text))


def print_colored_noLF(code, text, is_bold=False):
    if is_bold:
        code = '1;%s' % code
    print('\033[%sm%s\033[0m' % (code, text), end='')


# define color func
print_gray = partial(print_colored, '30')
print_red = partial(print_colored, '31')
print_green = partial(print_colored, '32')
print_yelow = partial(print_colored, '33')
print_blue = partial(print_colored, '34')
print_purple = partial(print_colored, '35')
print_cyan = partial(print_colored, '36')
print_gray_bg = partial(print_colored, '40')
print_red_bg = partial(print_colored, '41')
print_green_bg = partial(print_colored, '42')
print_yelow_bg = partial(print_colored, '43')
print_blue_bg = partial(print_colored, '44')
print_purple_bg = partial(print_colored, '45')
print_cyan_bg = partial(print_colored, '46')
print_bigwhite = partial(print_colored, '1')
print_offgray = partial(print_colored, '2')
print_underline = partial(print_colored, '4')
print_while_bg = partial(print_colored, '7')
print_cancelline = partial(print_colored, '9')
print_gray_noLF = partial(print_colored_noLF, '30')
print_red_noLF = partial(print_colored_noLF, '31')
print_green_noLF = partial(print_colored_noLF, '32')
print_yelow_noLF = partial(print_colored_noLF, '33')
print_blue_noLF = partial(print_colored_noLF, '34')
print_purple_noLF = partial(print_colored_noLF, '35')
print_cyan_noLF = partial(print_colored_noLF, '36')
print_gray_bg_noLF = partial(print_colored_noLF, '40')
print_red_bg_noLF = partial(print_colored_noLF, '41')
print_green_bg_noLF = partial(print_colored_noLF, '42')
print_yelow_bg_noLF = partial(print_colored_noLF, '43')
print_blue_bg_noLF = partial(print_colored_noLF, '44')
print_purple_bg_noLF = partial(print_colored_noLF, '45')
print_cyan_bg_noLF = partial(print_colored_noLF, '46')
print_bigwhite_noLF = partial(print_colored_noLF, '1')
print_offgray_noLF = partial(print_colored_noLF, '2')
print_underline_noLF = partial(print_colored_noLF, '4')
print_while_bg_noLF = partial(print_colored_noLF, '7')
print_cancelline_noLF = partial(print_colored_noLF, '9')


def check_color():
    print_gray('print_gray')
    print_red('print_red')
    print_green('print_green')
    print_yelow('print_yelow')
    print_blue('print_blue')
    print_purple('print_purple')
    print_cyan('print_cyan')
    print_gray_bg('print_gray_bg')
    print_red_bg('print_red_bg')
    print_green_bg('print_green_bg')
    print_yelow_bg('print_yelow_bg')
    print_blue_bg('print_bloe_bg')
    print_purple_bg('print_purple_bg')
    print_cyan_bg('print_cyan_bg')
    var1 = 'abc'
    var2 = 'def'
    print_red('a is %s\n b is %s' % (var1, var2))
    print_gray_noLF('print_gray_noLF')
    print_red_noLF('print_red_noLF')
    print_green_noLF('print_green_noLF')
    print_yelow_noLF('print_yelow_noLF')
    print_blue_noLF('print_blue_noLF')
    print_purple_noLF('print_purple_noLF')
    print_cyan_noLF('print_cyan_noLF')
    print_gray_bg_noLF('print_gray_bg_noLF')
    print_red_bg_noLF('print_red_bg_noLF')
    print_green_bg_noLF('print_green_bg_noLF')
    print_yelow_bg_noLF('print_yelow_bg_noLF')
    print_blue_bg_noLF('print_bloe_bg_noLF')
    print_purple_bg_noLF('print_purple_bg_noLF')
    print_cyan_bg_noLF('print_cyan_bg_noLF')
    print_red_noLF('a is %s\n b is %s' % (var1, var2))
    print_noLF('print_noLF')
    print_bigwhite('bigwhite')
    print_offgray('offgray')
    print_underline('underline')
    print_while_bg('while_bg')
    print_cancelline('cancelline')
    print_bigwhite_noLF('bigwhite')
    print_offgray_noLF('offgray')
    print_underline_noLF('underline')
    print_while_bg_noLF('while_bg')
    print_cancelline_noLF('cancelline')


if __name__ == '__main__':
    check_color()
