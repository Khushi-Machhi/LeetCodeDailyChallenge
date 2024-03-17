# 57. Insert Interval

    def insert(intervals, newInterval):
        newarr = []
        inserted = False
        for i in intervals:
            if inserted or i[1] < newInterval[0]:
                newarr.append(i)
            elif newInterval[1] < i[0]:
                newarr.append(newInterval)
                newarr.append(i)
                inserted = True
            else:
                newInterval[0] = min(newInterval[0], i[0])
                newInterval[1] = max(newInterval[1], i[1])
        
        if not inserted:
            newarr.append(newInterval)
        
        return newarr
    
