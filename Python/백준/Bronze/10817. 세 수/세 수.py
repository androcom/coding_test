def main():
    numbers = list(map(int, input().split()))
    numbers.sort() # 두 번째로 큰 수 = 두 번째로 작은 수
    print(numbers[1])
    
main()