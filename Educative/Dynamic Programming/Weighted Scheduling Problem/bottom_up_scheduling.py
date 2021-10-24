def lastConflict(index, schedule, isSorted=False):
    if not isSorted:
        schedule = sorted(schedule, key=lambda x: x[1])
    
    for i in range(index, -1, -1):
        if schedule[index][0] >= schedule[i][1]:
            return i
    return -1

def WeightedSchedule(schedule):
    schedule = sorted(schedule, key=lambda x: x[1])
    dp = [0 for i in range(len(schedule)+1)]

    for i in range(1, len(schedule)+1):
        index = lastConflict(i-1, schedule, isSorted=True)

        dp[i] = max(dp[i-1], dp[index+1] + schedule[i-1][2])
    return dp[len(schedule)]
        

print(WeightedSchedule([(0, 2, 25), (1, 5, 40), (6, 8, 170), (3, 7, 220)]))
schedule = [(i,i+2,10) for i in range(100)]
print(WeightedSchedule(schedule))
