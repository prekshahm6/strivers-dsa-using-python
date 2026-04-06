def countDigits(n):
    cnt = 0
    while n > 0:
        cnt = cnt + 1
        n = n // 10
    return cnt


if __name__ == "__main__":
    N = int(input("Enter a number: "))
    print("N:", N)
    digits = countDigits(N)
    print("Number of Digits in N:", digits)