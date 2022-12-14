class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l,r = 0,0
        hashmap = dict()
        maxlen = 0
        while r < len(fruits) and l <= r:
            if len(hashmap) < 2 or fruits[r] in hashmap:
                hashmap[fruits[r]] = 1 + hashmap.get(fruits[r],0)
                maxlen = max(maxlen,r-l+1)
                r+= 1
            else:
                maxlen = max(maxlen,r-l)
                while len(hashmap) >= 2:
                    hashmap[fruits[l]]-= 1
                    if hashmap[fruits[l]] == 0:hashmap.pop(fruits[l])
                    l+= 1  
        return maxlen
