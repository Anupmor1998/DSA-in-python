# Merge Intervals

def merge(intervals):
    intervals.sort()
    ans = [intervals[0]]
    i = 1
    while i < len(intervals):
        if intervals[i][0] <= ans[-1][1]:
            ans[-1] = [ans[-1][0], max(ans[-1][1], intervals[i][1])]
        else:
            ans.append(intervals[i])
        i += 1
    return ans
