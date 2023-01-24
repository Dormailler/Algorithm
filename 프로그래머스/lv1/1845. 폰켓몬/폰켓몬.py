def solution(nums):
    stack = []
    answer = 0
    n = len(nums) // 2
    for i in nums:
        if i not in stack:
            stack.append(i)
    answer = min(n,len(stack))
    return answer