import sys

def main():
    num_elements = int(sys.stdin.readline())
    counts = [0] * 10001

    for _ in range(num_elements):
        num = int(sys.stdin.readline())
        counts[num] += 1

    for i in range(10001):
        if counts[i] > 0:
            for _ in range(counts[i]):
                print(i)

main()