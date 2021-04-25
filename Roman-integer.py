class Solution:
    def romanToInt(self, s: str) -> int:
        r_numbers = {  'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, "C":100, "D" :500, "M":1000}
        #s = "MCMXCIV"#MCMXCIV
        number = 0
        i = 0
        j = 1
        while(i<len(s)):
            if(len(s)==1):
                number = r_numbers[s[0]]
                return number
            if s[i] != s[j] and i == j - 1 and r_numbers[s[i]]<r_numbers[s[j]]:
                number += r_numbers[s[j]] - r_numbers[s[i]]
                i += 2
                if(j<len(s)-2):
                    j += 2
                #j += 2
            else:
                number += r_numbers[s[i]]
                i+=1
                if(j<len(s)-1):
                    j+=1
                
        return number