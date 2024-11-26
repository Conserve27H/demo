# -*- coding: utf-8 -*-
"""
@Auth :YuanHan Zheng
"""


def str_reverse(s):
    return s[::-1]
# return print(list(reversed(s)))

def substr(s, x, y):
    return s[x: y]


if __name__ == '__main__':
    print(f'反转后的字符串为：{str_reverse("abcdefg")}')
    print(f'切片后的字符串为：{substr("sdffgsd", 0, 5)}')
