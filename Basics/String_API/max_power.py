def maxPower(self, s: str) -> int:
    b= 1
    w = 1
    for i in range(1,len(s)):

        if s[i] != s[i-1]:
            w = 1
        else:
            w+=1
            b = max(b,w)
    return b
                    
                
            