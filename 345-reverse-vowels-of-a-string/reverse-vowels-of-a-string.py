class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=["a","e","i","o","u"]
        rev_vowel=[]
        for ch in s:
            if ch.lower() in vowels:
                rev_vowel.append(ch)
        result=[]
        for ch in s:
            if ch.lower() in vowels:
                result.append(rev_vowel.pop())
            else:
                result.append(ch)
        return "".join(result)