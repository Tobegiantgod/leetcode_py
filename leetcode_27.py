class Solution(object):
	def removeElement(self, nums, val):
		"""
		:type nums: List[int]
		:type val: int
		:rtype: int
		"""
		if nums==[]:
			return 0
		i=0
		len_nums = len(nums)
		while i < len_nums:
			if nums[i]==val:
			    nums.pop(i)
			    len_nums-=1
			else:
			    i+=1
		return len_nums
