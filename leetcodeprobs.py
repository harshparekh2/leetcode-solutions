# Day 1 - TWO SUM
class Solution:
    def twoSum(self, nums, target):
        # Loop through each number (first number)
        for i in range(len(nums)):
            # Loop through each number again (second number)
            for j in range(i + 1, len(nums)):
                # Check if both numbers add up to target
                if nums[i] + nums[j] == target:
                    return [i, j]  # return their positions


# Day 2 - Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
