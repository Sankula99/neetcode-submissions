class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        hashmap_4result ={}
        for s in strs:
            sortedStr = ''.join((sorted(s)))
            if sortedStr not in hashmap:
                hashmap[sortedStr]= []
            hashmap[sortedStr].append(s)
        return list(hashmap.values())


        