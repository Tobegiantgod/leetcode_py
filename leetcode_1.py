class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        Inputlist = nums
        etarget = target/2.0
        smaller = 0
        bigger = 0
        for i in range(len(Inputlist)):
            if Inputlist[i]<=etarget:
                smaller = Inputlist[i]
            j=0
            for j in range(i+1,len(Inputlist)):
                if Inputlist[j]>=etarget:
                    bigger = Inputlist[j]
                if smaller+bigger == target:
                    return i,j
