class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        result = []

        for word in words:
            if len(word) <= 2:
                result.append(word.lower())
            else:
                result.append(word.capitalize()) 
                
        return ' '.join(result)

        