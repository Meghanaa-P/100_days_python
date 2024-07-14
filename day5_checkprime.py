def is_prime(number):
    if number <= 1:
        return False  
    elif number == 2:
        return True  
    elif number % 2 == 0:
        return False 
    else:
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        return True

num=int(input("Enter the number to check wheather the number id prime or not : "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

