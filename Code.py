class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = []
        if "000" in num:
            result.append(0)
        if "111" in num:
            result.append(111)
        if "222" in num:
            result.append(222)
        if "333" in num:
            result.append(333)
        if "444" in num:
            result.append(444)
        if "555" in num:
            result.append(555)
        if "666" in num:
            result.append(666)
        if "777" in num:
            result.append(777)
        if "888" in num:
            result.append(888)
        if "999" in num:
            result.append(999)
        
        maxi =-1
        for i in result:
            maxi = max(maxi, i)
        
        if maxi == 0:
            return "000"
        if maxi==-1:
            return ""
        
        return str(maxi)
