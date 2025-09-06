def solution(x, n):
    if x > 0:
        answer = [num for num in range(x, x*n + 1, x)]
    elif x < 0:
        answer = [num for num in range(x, x*n - 1, x)]
    else:
        answer = [0 for _ in range(n)]
    return answer