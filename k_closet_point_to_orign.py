class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sorted = []
        output = []
        for point in points:
            distance = point[0]**2+point[1]**2
            sorted.append([distance,point])
        sorted.sort()
        for i in range(k):
            output.append(sorted[i][1])
        return output
