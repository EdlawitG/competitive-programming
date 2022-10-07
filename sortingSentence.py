class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        n = len(words)
        for i in range(n-1):
            for j in range(i+1, n):
                if words[i][-1] > words[j][-1]:
                    words[i], words[j] = words[j], words[i]
        return " ".join([word[:-1] for word in words])
