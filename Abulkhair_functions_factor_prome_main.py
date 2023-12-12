def smallest_factor(n):
    if n < 2:
        return None
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return n

def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

while True:
    print("Menu:")
    print("1. Find the smallest factor of a number")
    print("2. Find prime numbers in a range")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 0:
        print("Program terminated.")
        break
    elif choice == 1:
        num = int(input("Enter a number: "))
        factor = smallest_factor(num)
        if factor is None:
            print(f"{num} is less than 2.")
        else:
            print(f"The smallest factor of {num} is: {factor}")
    elif choice == 2:
        start = int(input("Enter the starting number: "))
        end = int(input("Enter the ending number: "))

        if end <= start:
            print(f"Enter a number greater than {start}.")
            continue

        primes = find_primes_in_range(start, end)
        print(f"Prime numbers between {start} and {end} are:")
        for prime in primes:
            print(prime)
    else:
        print("Invalid choice. Please enter 0, 1, or 2.")