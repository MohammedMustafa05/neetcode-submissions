class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        count = 0

        for n in num_set:
            if n - 1 not in num_set:
                subseq = 1
                while n + subseq in num_set:
                    subseq += 1
                count = max(subseq, count)
    
        return count