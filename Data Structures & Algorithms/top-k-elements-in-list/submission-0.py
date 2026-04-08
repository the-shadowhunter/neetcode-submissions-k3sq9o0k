class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        heap=[]
        for i in range(len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1
        for num,count in freq.items():
            heapq.heappush(heap,(count,num))
            if len(heap)>k:
                heapq.heappop(heap)
            
        return [num for count,num in heap]
        