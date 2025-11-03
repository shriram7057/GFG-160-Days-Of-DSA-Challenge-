class Solution:    
    def minPlatform(self, arr, dep):
        arr.sort()
        dep.sort()
        
        n = len(arr)
        i = j = 0
        platforms = 0
        max_platforms = 0
        
        while i < n and j < n:
            if arr[i] <= dep[j]:
                platforms += 1
                i += 1
            else:
                platforms -= 1
                j += 1
            max_platforms = max(max_platforms, platforms)
        
        return max_platforms
