class Solution:
    def reverse(self, x: int) -> int: 
            x = str(x)                       # turn to string
            x = x[::-1]                      # reverse it 
            if len(x) == 1:# if number is itself, no need to reverse
                return int(x)
            if x[-1] == "-": #if it was negative, has a minus in the end
                x = x.replace("-" , "") #REMOVE THE MINUS
                x = "-" + x             #Add the minus in the start
            if  -2**31 < int(x) < 2**31 - 1 : 
                return int(x)
            return 0 
        