def main():
    n_num = int(input())
    w_list = []
    for _ in range(n_num):
        w_list.append(input())
    w_list = list(set(w_list))
    w_list.sort(key=lambda w: (len(w), w))
    for w in w_list:
        print(w)
main()