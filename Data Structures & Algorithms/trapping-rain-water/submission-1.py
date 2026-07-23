class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1

        if not height:
            return 0

        leftmax,rightmax=height[l],height[r]
        res=0
        while l<r:
            if leftmax<rightmax:
                leftmax+=1
                res=leftmax-height[l]

            else:
                r-=1
                rightmax
                res=rightmax-height[r]

        return res
