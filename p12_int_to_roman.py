class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""

        def get_thousands():
            thousands = num // 1000
            return "M" * thousands

        def get_hundreds():
            hundreds = (num % 1000) // 100            
            if hundreds == 9:
                return "CM"
            elif hundreds >= 5:
                return "D" + "C" * (hundreds - 5)
            elif hundreds == 4:
                return "CD"
            else:
                return "C" * hundreds
        def get_tens():
            tens = (num % 100) // 10
            if tens == 9:
                return "XC"
            elif tens >= 5:
                return "L" + "X" * (tens - 5)
            elif tens == 4:
                return "XL"
            else:
                return "X" * tens
        def get_ones():
            ones = num % 10
            if ones == 9:
                return "IX"
            elif ones >=5:
                return "V" + "I" * (ones - 5)
            elif ones ==4:
                return "IV"
            else:
                return "I" * ones

        if num > 999:
            res += get_thousands() + get_hundreds() + get_tens() + get_ones()
        elif num > 99:
            return get_hundreds() + get_tens() + get_ones()
        elif num > 9:
            return get_tens() + get_ones()
        else:
            return get_ones()
def main():
    s = Solution()
    print(s.intToRoman(1994))


