class Solution:
    def clearDigits(self, s: str) -> str:
        res = []
        for i in s:
            if(i>='0' and i<='9'):
                if len(res) > 0:
                    res.pop()
            else:
                res.append(i)
        return "".join(res)

        