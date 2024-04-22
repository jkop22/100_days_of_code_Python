num = int(input("Enter number to check: "))

def prime_checker(num):
    if num <= 1:
        print(f"{num} IS NOT prime.")
    elif num <= 3:
        print(f"{num} IS prime.")
    else:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
        if is_prime:
            print(f"Number {num} IS prime.")
        else:
            print(f"Number {num} IS NOT prime.")

prime_checker(num)

        