class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # floor division? ok wait this problem isn't as easy as that. 
        # the array already has 1s in it.
        # I need to figure out how much space is left
        # how many spaces of 'concurrent 0s' are there

        # 'the sliding window' 
        # there's two pointers. one to the beginning, one to the end. 
        freeslots = 0

        # print([plot for plot in range(len(flowerbed)) if flowerbed[plot]==0])

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left_empty = (i == 0 or flowerbed[i-1] == 0)
                right_empty = (i == (len(flowerbed)-1) or flowerbed[i+1]==0)
                if left_empty and right_empty == True:
                    flowerbed[i] = 1
                    freeslots += 1
        
        if n <= freeslots:
            return True
        else:
            return False
        