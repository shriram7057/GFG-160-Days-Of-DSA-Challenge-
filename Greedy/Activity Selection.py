class Solution:
    def activitySelection(self, start, finish):
        # Pair start and finish times
        activities = list(zip(start, finish))
        # Sort by finish time
        activities.sort(key=lambda x: x[1])
        
        count = 1  # Select the first activity
        last_end = activities[0][1]
        
        for i in range(1, len(activities)):
            if activities[i][0] > last_end:
                count += 1
                last_end = activities[i][1]
        
        return count
