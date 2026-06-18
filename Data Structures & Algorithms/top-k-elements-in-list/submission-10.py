class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap= {}
        listr = []
        for num in nums:
            if(num not in hashmap):
                hashmap[num]= 1
            else:
                hashmap[num]+=1
        sorted_hash=sorted(hashmap.items(), key = lambda x:x[1], reverse =True)
        for i in range(k):
            listr.append(sorted_hash[i][0])

        return listr