#11650번
def main():
    n_num = int(input())
    p_list = []
    for _ in range(n_num):
        p_list.append(tuple(map(int, input().split())))
    p_list = sorted(p_list)
    for p in p_list:
        print(p[0], p[1])
main()