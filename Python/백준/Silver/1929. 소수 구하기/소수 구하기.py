def main():
    start_num, end_num = map(int, input().split())
    prime_list = [True] * (end_num + 1)
    prime_list[0] = False
    prime_list[1] = False
    
    for i in range(2, end_num+1):
        if prime_list[i]:
            for j in range(i*i, end_num+1, i):
                prime_list[j] = False
    
    for i in range(start_num, end_num+1):
        if prime_list[i] == True:
            print(i)
main()