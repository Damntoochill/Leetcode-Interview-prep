class Solution:
    def reverse(self, x: int) -> int:
        rx = 0
        flag = 0
        if x<0:
            flag = 1
        x = abs(x)
        while(x):
            digit = x%10
            rx = rx*10 + digit
            x = x//10
        if (-2**31 <= rx <= 2**31 - 1):
            if flag == 1:
                return -rx
            else:
                return rx
        else:
            return 0
        
            
        
