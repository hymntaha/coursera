# python3
import sys

def sum_of_two_digits(first_digit, second_digit):
    return int(first_digit) + int(second_digit)

if __name__ == '__main__':
    var1, var2 = input().split()

    try:
        val1 = int(var1)
        val2 = int(var2)
    except ValueError:
        var1, var2 = input().split()


    if (int(var1) >= 0 and int(var1) <= 9) and (int(var2)>=0 and int(var2)<=9):
        sum = sum_of_two_digits(var1, var2)
    else:
        print("The numbers need to be in between 0 to 9")
    # Add two numbers

    print(sum)
