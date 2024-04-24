def factorial(n):
    res = n
    if n == 0:
        res = 1
    else:
        for i in range(1, n):
            res *= i
    return res
    
num = int(input("Enter number U wanna factorial from: "))
print(f"{num}! is {factorial(num)}.")
    
    




