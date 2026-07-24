class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        l=1
        r=x

        while l<=r:
            mid=(l+r)//2
            midsq=mid*mid   
            if midsq>x:
                r=mid-1
            else:
                ans=mid
                l=mid+1

        return ans