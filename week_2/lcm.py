# Uses python3
# import time
# start_time = time.time()

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm_naive(a, b):
    return a * b // gcd(a, b)

if __name__ == '__main__':
    input = input()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))
    # print("--- %s seconds ---" % (time.time() - start_time))

