class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]

        minLen = min(len(a), len(b))
        c = '0'
        s = '0'

        res = ''

        for i in range(minLen):
            if a[i] == '0' and b[i] == '0':
                if c == '1':
                    s = '1'
                    c = '0'
                else:
                    s = '0'
            elif a[i] == '0' and b[i] =='1' \
                    or a[i] == '1' and b[i] == '0':
                if c == '1':
                    s = '0'
                else:
                    s = '1'
            else:
                if c == '0':
                    s = '0'
                    c = '1'
                else:
                    s = '1'
            
            res += s
        
        rem = a[minLen:] if len(a) > minLen else b[minLen:]

        for i in range(len(rem)):
            if c == '0' and rem[i] == '0':
                s = '0'
            elif c == '0' and rem[i] == '1' \
                    or c == '1' and rem[i] == '0':
                s = '1'
                c = '0'
            else:
                s = '0'
                c = '1'
        
            res += s
        
        if c == '1':
            res += '1'
        
        return res[::-1]
