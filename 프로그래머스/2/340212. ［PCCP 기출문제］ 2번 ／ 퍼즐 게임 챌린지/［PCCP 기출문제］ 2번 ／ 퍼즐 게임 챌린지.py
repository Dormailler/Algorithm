def solution(diffs, times, limit):
    def is_possible(level):
        time = stime
        for i in range(l):
            if diffs[i] > level:
                extra = (diffs[i] - level) * (times[i] + times[i-1])
                time += extra
                if time > limit:
                    return False
        return True

    md = max(diffs)
    stime = sum(times)
    l = len(diffs)

    # 이진 탐색
    left, right = 1, md
    answer = md
    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer