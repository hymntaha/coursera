# Uses python3

def calc_fib(n):
    x,y = 0, 1
    for i in range(n):
        x, y = y, x + y
    return x

n = int(input())
print(calc_fib(n))