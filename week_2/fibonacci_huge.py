# Uses python3
# import time
# start_time = time.time()

def get_fibonacci_huge_naive(n):
    if n == 0:
        return (0, 1)
    else:
        num1, num2 = get_fibonacci_huge_naive(n // 2)
        result1 = num1 * (num2 * 2 - num1)
        result2 = num1 * num1 + num2 * num2
        if n % 2 == 0:
            return (result1, result2)
        else:
            return (result2, result1 + result2)

if __name__ == '__main__':
    input = input();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n)[0] % m)
    # print("--- %s seconds ---" % (time.time() - start_time))
