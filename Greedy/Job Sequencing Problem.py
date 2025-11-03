class Solution:
    def jobSequencing(self, deadline, profit):
        jobs = list(zip(deadline, profit))
        jobs.sort(key=lambda x: x[1], reverse=True)
        
        max_deadline = max(deadline)
        slots = [False] * max_deadline
        total_profit = 0
        job_count = 0
        
        for d, p in jobs:
            for i in range(d - 1, -1, -1):
                if not slots[i]:
                    slots[i] = True
                    total_profit += p
                    job_count += 1
                    break
                    
        return job_count, total_profit
