# 각 자릿수의 합을 반환하는 함수
def d(n):
    return n + sum(map(int, str(n)))

def main():
    """
    생성자를 여러개 갖는 경우가 있음
    > 중복을 제거하기 위해 set 사용
    """
    all_numbers = set(range(1, 10001))
    generated_numbers = set()

    for i in range(1, 10001):
        generated_numbers.add(d(i))
        
    self_numbers = sorted(all_numbers - generated_numbers)
    
    for num in self_numbers:
        print(num)

main()