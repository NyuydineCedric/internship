def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def filter_primes(numbers):
    primes = []

    for number in numbers:
        if is_prime(number):
            primes.append(number)

    return primes


numbers = [4, 6, 7, 9, 10, 13, 15, 16, 17, 18, 19,21]

print(filter_primes(numbers))