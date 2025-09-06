import sys

def main():
    N = int(sys.stdin.readline())
    counts = [0] * 10001    # index와 num 범위 일치

    for _ in range(N):
        num = int(sys.stdin.readline())
        counts[num] += 1    # 입력횟수

    for i in range(10001):
        if counts[i] > 0:
            for _ in range(counts[i]):
                print(i)

main()
