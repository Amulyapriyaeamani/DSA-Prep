def reverse_number(n):
    rev = 0
    while n != 0:
        last = n % 10
        rev = rev * 10 + last
        n //= 10
    return rev

# Example usage
n = int(input("Enter a number: "))
print("Reversed Number:", reverse_number(n))
