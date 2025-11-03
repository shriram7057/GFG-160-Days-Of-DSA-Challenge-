class Solution:
    def maxPartitions(self, s):
        last_index = {}
        for i, ch in enumerate(s):
            last_index[ch] = i

        partitions = 0
        end = 0

        for i, ch in enumerate(s):
            end = max(end, last_index[ch])
            if i == end:
                partitions += 1

        return partitions
