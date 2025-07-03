def count_digits(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count

# Example usage
n = int(input("Enter a number: "))
print("Number of digits:", count_digits(n))
