from collections import defaultdict
from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(list)

        # Initialize buckets
        for word in words:
            waiting[word[0]].append(word)

        count = 0

        # Traverse s once
        for c in s:
            current = waiting[c]
            waiting[c] = []

            for word in current:
                if len(word) == 1:
                    count += 1
                else:
                    waiting[word[1]].append(word[1:])

        return count
