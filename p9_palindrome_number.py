#!/usr/bin/env python3
# File: palindrome_number.py

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            digits = []
            while x > 0:
                digits.append(x % 10) # 从个位数开始加入除以10的余数，即各位的数字。
                x = x // 10           # 丢弃已加入的最后一位数字。
            if digits == digits[::-1]:
                return True
            else:
                return False
