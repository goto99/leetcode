#!/usr/bin/env python
# File: Z_transformation.py

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        考虑周期性，以第一列开始，到第二个完整的列之前为一个周期，numRows=3时，一个周期有4(numRows*2-2)个字符，
        numRows=4时，一个周期有6(numRows*2-2)个字符……
        numRows小于3时，一个周期的字符数与numRows相等；
        """
        if numRows < 3:
            period = numRows
        else:
            period = numRows * 2 - 2

        groups = [] # 将每个周期的子字符串储存到列表中来
        start = 0
        end = period
        while end < len(s):
            groups.append(s[start: end])
            start = end
            end += period
        groups.append(s[start:]) # 对字符串s中最后剩下的不足一个周期的字符，单独加到列表的最后。
        groups[-1] = groups[-1] + ' ' * (period - len(groups[-1])) # 最后一组不够一个周期的，用空格补齐长度，以便统一处理；

        output = ''
        for i in range(numRows):
            for substr in groups:
                if i == 0 or i == period / 2:
                    output += substr[i]
                else:
                    output += substr[i] + substr[-i]

        return output.replace(' ', '') # 把最后一组的空格替换掉。
