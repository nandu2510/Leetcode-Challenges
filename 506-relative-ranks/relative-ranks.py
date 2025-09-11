from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Sort the scores but keep their original index
        sorted_scores = sorted([(s, i) for i, s in enumerate(score)], reverse=True)

        # Create a result list with the same size as input
        res = [''] * len(score)

        # Assign medals or ranks
        for rank, (s, i) in enumerate(sorted_scores):
            if rank == 0:
                res[i] = "Gold Medal"
            elif rank == 1:
                res[i] = "Silver Medal"
            elif rank == 2:
                res[i] = "Bronze Medal"
            else:
                res[i] = str(rank + 1)

        return res
