def solution(mats, park):
    answer = 0
    mats.sort(reverse=True)
    for mat in mats:
        for i in range(len(park)):
            for j in range(len(park[0])):
                k = 0
                for m1 in range(mat):
                    for m2 in range(mat):
                        if i+m1 >= len(park) or j+m2 >= len(park[0]):
                            k = 1
                            continue
                        if park[i+m1][j+m2] != "-1":
                            k = 1
                            continue
                if k == 0:
                    return mat
    return -1