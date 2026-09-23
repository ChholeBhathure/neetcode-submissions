class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map={}
        result=[]
        for num in nums:
            if num not in freq_map:
                freq_map[num]=1
            else:
                freq_map[num]+=1
        bucket=[[] for _ in range(len(nums)+1)]
        for key in freq_map:
            bucket[freq_map[key]].append(key)
        for i in range (len(bucket)-1,0,-1):
            for num in bucket[i]:
                result.append(num)
                if len(result)==k:
                    return result