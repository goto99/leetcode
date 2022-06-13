class Solution:
    def intToRoman(self, num: int) -> str:
        thousands = num // 1000
        hundreds = (num % 1000) // 100
        tens = (num % 100) // 10
        ones = num % 10 

        res = "M" * thousands

        if hundreds == 9:
            res += "CM"
        elif hundreds >= 5:
            res += "D" + "C" * (hundreds - 5)
        elif hundreds == 4:
            res += "CD"
        else:
            res += "C" * hundreds

        if tens == 9:
            res += "XC"
        elif tens >= 5:
            res += "L" + "X" * (tens -5)
        elif tens == 4:
            res += "XL"
        else:
            res += "X" * tens
        
        if ones == 9:
            res += "IX"
        elif ones >=5:
            res += "V" + "I" * (ones - 5)
        elif ones ==4:
            res += "IV"
        else:
            res += "I" * ones
        
        return res    



