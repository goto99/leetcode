#!/usr/bin/env python
# File: pow_x_n.py
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        import sys
        # 特例1，如果x无限接近1或-1，不进行计算，根据n值决定返回1或-1。
        if abs(abs(x)-1.0) < sys.float_info.min:
            if x < 0 and n%2 == 0:
                return -x
            else:
                return x
        sign = 1
        if n < 0: 
            n = -n
            sign = -1
        i = 1
        result = 1.0
        if sign > 0:
            while i <= n:
                result *= x
                # 特例2，如果结果无限接近于0，返回0，不再计算；
                if abs(result) <= sys.float_info.min:
                    return 0.0
                # 特例3，如果结果上溢出，返回最大的float值，不再计算；
                elif result > sys.float_info.max:
                    return sys.float_info.max
                # 特例4，如果结果下溢出，返回最小的float值，不再计算；
                elif result < - sys.float_info.max:
                    return -sys.float_info.max
                i += 1
        else:
            while i <= n:
                result /= x
                if abs(result) <= sys.float_info.min:
                    return 0.0
                elif result > sys.float_info.max:
                    return sys.float_info.max
                elif result < - sys.float_info.max:
                    return -sys.float_info.max
                i += 1
        return result
