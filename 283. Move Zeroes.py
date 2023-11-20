class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #setting the counter to 0
        count = 0
        if len(nums) >= 1:
            if 0 in nums:
                # counting the number of 0's
                for i in nums:
                    if i == 0:
                        count = count+1
                # Remove the 0's and append them (Note: Append will always add values in the end of list)
                for i in range(0,count):
                    nums.remove(0)
                    nums.append(0)
        # if list has no 0's or has only 1 element, return as it s
        else:
            return nums

        
