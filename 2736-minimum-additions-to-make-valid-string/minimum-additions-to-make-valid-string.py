class Solution:
    def addMinimum(self, word: str) -> int:

        # return len(word.replace('abc','' )
        #                .replace('ab' ,'C' )
        #                .replace('ac' ,'B' )
        #                .replace('bc' ,'A' )
        #                .replace('a'  ,'AA')
        #                .replace('b'  ,'BB')
        #                .replace('c'  ,'CC')
        #                .replace('X'  ,''  ))
       
        count = 1  # At least one block
        for i in range(1, len(word)):
            if word[i] <= word[i - 1]:
                count += 1
        return count * 3 - len(word)
