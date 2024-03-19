# 621. Task Scheduler

 def leastInterval(tasks, n):
        task_counts = Counter(tasks)
        
        max_freq = max(task_counts.values())
        c = sum(1 for count in task_counts.values() if count == max_freq)
        
        total_intervals = (max_freq - 1) * (n + 1) + c
        
        return max(total_intervals, len(tasks))
