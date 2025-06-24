# Recursive function to check if a number is prime
def is_prime_recursive(n, i=2):
    if n <= 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return is_prime_recursive(n, i + 1)

# Sample input
num_of_employees = 6
scores = [23, 77, 54, 81, 48, 34]

# Count prime scores using recursive prime checker
prime_count = sum(1 for score in scores if is_prime_recursive(score))

# Output result
print(prime_count)
