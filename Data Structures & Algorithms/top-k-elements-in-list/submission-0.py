class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data={}
        for i in range(len(nums)):
            data[nums[i]]=1+data.get(nums[i],0)
        data=dict(sorted(data.items(),key=lambda item:item[1],reverse=True))
        return list(data.keys())[0:k]