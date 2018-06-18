# Uses python3
import sys

def get_change(m):
    coins = [1,5,10]
    count, n = len(coins) + 1, int(m) + 1
    table = [[0] * n for x in range(count)]

    for j in range(1, n):
        table[0][j] = float('inf')
    for i in range(1, count):
        for j in range(1, n):
            aC = table[i][j - coins[i - 1]] if j - coins[i - 1] >= 0 else float('inf')
            table[i][j] = min(table[i - 1][j], 1 + aC)
    return table[count - 1][n - 1]

if __name__ == '__main__':
    m = input()
    print(get_change(m))
