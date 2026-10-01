class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maximum=0
        sequence=set(nums)
        for num in sequence:
            if (num-1) not in sequence:
                curr_num=num
                count=1
                while (curr_num+1) in sequence:
                    curr_num+=1
                    count+=1
                maximum=max(maximum,count)
        return maximum
        