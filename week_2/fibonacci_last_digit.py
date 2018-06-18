# Uses python3
# import time
# start_time = time.time()

def get_fibonacci_last_digit_naive(n):
    if n == 0:
        return (0, 1)
    else:
        num1, num2 = get_fibonacci_last_digit_naive(n // 2)
        result1 = num1 * (num2 * 2 - num1)
        result2 = num1 * num1 + num2 * num2
        if n % 2 == 0:
            return (result1, result2)
        else:
            return (result2, result1 + result2)

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_naive(n)[0] % 10)
    # print("--- %s seconds ---" % (time.time() - start_time))