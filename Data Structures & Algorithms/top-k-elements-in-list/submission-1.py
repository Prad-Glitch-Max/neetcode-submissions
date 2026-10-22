class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # data={}
        # for i in range(len(nums)):
        #     data[nums[i]]=1+data.get(nums[i],0)
        # data=dict(sorted(data.items(),key=lambda item:item[1],reverse=True))
        # return list(data.keys())[0:k]
        count={}
        for n in nums:
            count[n]=1+count.get(n,0)
        buckets=[[] for _ in range(len(nums)+1)]
        for num,freq in count.items():
            buckets[freq].append(num)
        res=[]
        for freq in range(len(buckets)-1,0,-1):
            for num in buckets[freq]:
                res.append(num)
                if len(res)==k:
                    return res
