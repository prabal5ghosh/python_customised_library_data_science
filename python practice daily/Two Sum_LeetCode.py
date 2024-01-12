# # -*- coding: utf-8 -*-
# """
# Created on Sun Dec 17 10:04:01 2023

# @author: praba
# """

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         try:
#             for i in nums:
                
#                 for j in range( nums.index(i)+1,len(nums)):
#                     m=0
#                     m=i+ nums[j]
#                     if m == target:
#                         print(f'index1: {nums.index(i)} and index2: {j}')
#                         return
#             raise Exception()
        
                    
#         except:
#             print("Sorry, no numbers in the array is not able to generate the target") 
                
        
# obj1=Solution()
# obj1.twoSum([3,5,7,1,9,3], 8)
    