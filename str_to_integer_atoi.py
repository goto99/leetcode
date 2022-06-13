#!/usr/bin/env python3
# File: str_to_integer_atoi.py

class Solution:
    def myAtoi(self, s: str) -> int:
        #先处理题目第一条要求
        s = s.lstrip(' ')

        #处理第二条要求
        if len(s) == 0:
            return 0

        sign = +1
        if s.startswith('-'):
            sign = -1
            s = s[1:]
        elif s.startswith('+'):
            s = s[1:]

        #读入数字
        digits = ''
        for c in s:
            if c in '0123456789':
                digits += c
            else:
                break
        digits.lstrip('0')
        if len(digits) == 0:
            return 0

        result = sign * int(digits)
        lower_limit = - 2 ** 31
        upper_limit = 2 ** 31 - 1
        if result < lower_limit:
            result = lower_limit
        elif result > upper_limit:
            result = upper_limit
        return result

