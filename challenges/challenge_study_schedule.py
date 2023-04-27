def study_schedule(permanence_period, target_time) -> int:
    count = 0
    for start, end in permanence_period:
        if start is None or end is None or target_time is None:
            return None
        if isinstance(start, int) and isinstance(end, int) and start <= target_time <= end:
            count += 1
        else:
            return None
    return count
