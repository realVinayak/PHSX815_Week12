def get_meaned_interval(intervals):
    meaned_list = []
    for interval_index in range(len(intervals)-1):
        meaned_list.append((intervals[interval_index]+intervals[interval_index+1])/2)
    return meaned_list