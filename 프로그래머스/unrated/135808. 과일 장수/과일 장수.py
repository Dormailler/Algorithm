def solution(k, m, score):
    st =[]
    score = sorted(score,reverse=True)
    i = 0
    answer = 0
    while i+m <= len(score):
        st.append(score[i:i+m])
        i += m
    for i in st:
        answer += m*min(i)
    return answer