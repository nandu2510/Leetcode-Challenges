class Solution:
    def reverseWords(self, s: str) -> str:
        # words_list=s.strip().split()
        # words_list.reverse()
        # return ' '.join(words_list)
        words=s.strip().split()
        words.reverse()
        return ' '.join(words)