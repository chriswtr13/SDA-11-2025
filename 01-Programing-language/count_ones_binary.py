def count_ones(n):
    count = bin(n).count("1")
    print(count)

def count_ones1(n):
    count = 0
    while n:
        count += n & 1  # Check if the last bit is 1
        n >>= 1         # Right-shift by 1
    return count

def count_ones2(n):
    count = 0
    while n:
        n &= (n - 1)  # Remove the lowest set bit
        count += 1
    return count

print(count_ones2(20))  # Output: 4




count_ones(-2)
print(count_ones1(-2))