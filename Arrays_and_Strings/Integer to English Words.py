"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Solution : Check if billionth, millionth, thousandth components are there

"""

class Solution:
    def numberToWords(self, num: int) -> str:
        def one(num):
            strings = {
                1 : 'One',
                2: 'Two', 
                3: 'Three', 
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine',
            }
            return strings[num]
        
        def two_lessthan20(num):
            strings = {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen'
            }
            return strings[num]
        
        def ten(num):
            strings = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety',
            }
            return strings[num]
        
        def two(num):
            if not num:
                return ''
            if num < 10:
                return one(num)
            elif num < 20:
                return two_lessthan20(num)
            else:
                tenner = num//10
                rest = num - tenner*10
                return ten(tenner) + ' ' + one(rest) if rest else ten(tenner)
            
        def three(num):
            hundred = num//100
            rest = num - hundred*100
            if hundred and rest:
                return one(hundred) + ' Hundred ' + two(rest)
            elif hundred and not rest:
                return one(hundred) + ' Hundred'
            elif not hundred and rest:
                return two(rest)
                
            
        billion = num//1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = ((num - billion * 1000000000) - million* 1000000)//1000
        rest = (((num - billion * 1000000000) - million* 1000000) - thousand * 1000)
        if not num:
            return 'Zero'
        res = ''
        if billion:
            res+= three(billion) + ' Billion'
        if million:
            res+= ' ' if res else ''
            res+= three(million) + ' Million'
        if thousand:
            res+= ' ' if res else ''
            res+= three(thousand) + ' Thousand'
        if rest:
            res+= ' ' if res else ''
            res+= three(rest)
        return res

s = Solution()
print(s.numberToWords(1234567891))