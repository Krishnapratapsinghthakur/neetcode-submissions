class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for num in nums:
            if num in freq:
                freq[num]=freq[num]+1
            else:
                freq[num]=1

        # result = sorted(
        #     freq.items(),
        #     key=lambda x: x[1],
        #     reverse=True
        # )[:k]

        # answer=[]

        # for i in result:
        #     answer.append(i[0])

        # return answer

        #with bucket sort 

        buckets = [[] for _ in range(len(nums)+1)]


        for num,count in freq.items():
            buckets[count].append(num)

        answer=[]

        for i in range(len(nums),0,-1):
            for num in buckets[i]:
                answer.append(num)
            if len(answer)>=k:
                return answer[:k]
        