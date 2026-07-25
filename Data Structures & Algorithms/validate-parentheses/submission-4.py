class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '[]' in s or '{}' in s :
            s.replace('()','')
            s.replace('[]','')
            s.replace('{}','')

        return s == ''