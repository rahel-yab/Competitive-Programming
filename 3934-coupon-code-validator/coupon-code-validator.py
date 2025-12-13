class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        businesses = ['electronics' , 'grocery' , 'pharmacy' , 'restaurant']
        code_b = list(zip(businessLine, code, isActive))
        code_b.sort()
        ans = []
        for x , y , z in code_b:
            flag = True
            for i in y:
                if not i.isalnum() and i != '_':
                    flag = False
                    break
            if z and flag and y and x in businesses:
                ans.append(y)

        return ans
                    
