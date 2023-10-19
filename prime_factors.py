#Write a function that generates factors for a given number.

def prime_factors(n):
    lst = []
    for i in range(1,10):
        if n%i == 0:
            lst.append(i)
    return lst

print(prime_factors(8))