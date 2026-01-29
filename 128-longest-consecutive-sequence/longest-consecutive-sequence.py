class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        longest = 0

        for num in st:
            if (num - 1) not in st:
                count = 1
                x = num
                while (x + 1) in st:
                    count += 1
                    x += 1
                longest = max(longest, count)

        return longest
