# Uses python3

def gcd_naive(a, b):
    while (b):
        a, b = b, a % b
    return a

if __name__ == "__main__":
    input = input()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
