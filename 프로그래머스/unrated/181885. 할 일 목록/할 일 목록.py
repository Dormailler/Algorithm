def solution(todo_list, finished):
    a = 0
    for i in range(len(finished)):
        if finished[i]:
            todo_list.pop(i-a)
            a += 1
    return todo_list