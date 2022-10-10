class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        people.sort()
        i = 0
        j = len(people)-1
        while i <= j:
            count += 1
            if people[i]+people[j] <= limit:
                i+=1
            j-=1
        return count
