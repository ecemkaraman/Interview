# interval merge
# definition: interval = [start, end]
def add_interval(new_interval, intervals):
    if intervals and intervals[-1][1] >= new_interval[0]:
        if intervals[-1][1] < new_interval[1]:
            intervals[-1][1] = new_interval[1]
    else:
        intervals.append(new_interval)