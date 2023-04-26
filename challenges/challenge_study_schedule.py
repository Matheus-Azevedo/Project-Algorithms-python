def study_schedule(permanence_period, target_time) -> int:
    if target_time is None or type(target_time) != int:
        return None
    count = 0
    for start, end in permanence_period:
        if start is None or end is None:
            return None
        if type(start) != int or type(end) != int:
            return None
        if start <= target_time <= end:
            count += 1
    return count
