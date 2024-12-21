# Write a function to check if a number is a Mersenne Prime.
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def is_mersenne_prime(mersenne_number):
    """Check if a number is a Mersenne prime."""
    # Check if the number is of the form 2^n - 1
    n = 1
    while True:
        mersenne_candidate = (1 << n) - 1  # This is 2^n - 1
        if mersenne_candidate > mersenne_number:
            return False
        if mersenne_candidate == mersenne_number:
            # Now check if n is prime
            return is_prime(n)
        n += 1

# Example usage:
number_to_check = 3
if is_mersenne_prime(number_to_check):
    print(f"{number_to_check} is a Mersenne prime.")
else:
    print(f"{number_to_check} is not a Mersenne prime.")