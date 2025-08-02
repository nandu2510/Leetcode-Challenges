class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        m1 = Counter(word1)
        s1 = list()
        m2 = Counter(word2)
        for i in m1:
            if i not in m2:
                return False
            s1.append(m1[i])
        
        for i in m2:
            if m2[i] not in s1:
                return False
            else:
                s1.remove(m2[i])
        
        return True
        