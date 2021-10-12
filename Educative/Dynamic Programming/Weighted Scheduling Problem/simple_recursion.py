def lastNonConflict(index, schedule, isSorted=False):
    if not isSorted:
        schedule = sorted(schedule, key=lambda x: x[1])
    
    for i in range(index, -1, -1):
        if schedule[index][0] >= schedule[i][1]:
            return i
    return None

def WSrecursive(schedule, n):
    if n == None or n < 0:
        return 0
    if n == 0:
        return schedule[n][2]

    return max(schedule[n][2] + WSrecursive(schedule, lastNonConflict(n, schedule, isSorted=True)), WSrecursive(schedule, n-1))

def WeightedSchedule(schedule):
    schedule = sorted(schedule, key=lambda x: x[1])
    return WSrecursive(schedule, len(schedule)-1)

schedule = [(0,2,25), (1,5,40), (6,8,170), (3,7,220)]
print(WeightedSchedule(schedule))
