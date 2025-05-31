def power(n: int):
    return True if (n > 0 and (n & (n-1)) == 0) else False

print(power(16))