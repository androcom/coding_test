def main():
    n_num, k_num = map(int, input().split())
    coin_list = []
    for _ in range(n_num):
        coin_list.append(int(input()))
    coin_list = sorted(coin_list,reverse=True) 
    count = 0
    for coin in coin_list:
        if coin <= k_num:
            count += k_num // coin
            k_num %= coin
    print(count)
main()