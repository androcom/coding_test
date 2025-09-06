def main():
    p_num = int(input())
    t_list = sorted(list(map(int, input().split())))
    min_t_num = 0
    for i in range(p_num):
        for j in range(i+1):
            min_t_num += t_list[j]
    print(min_t_num)
main()