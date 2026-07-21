class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l,r=len(word1),len(word2)
        res=[]
        for i in range(max(l,r)):
            if i<l:
                res.append(word1[i])
            if i<r:
                res.append(word2[i])
        return "".join(res)