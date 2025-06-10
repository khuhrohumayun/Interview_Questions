


            # Create a generator to produce first n prime numers


'''
Q: Create a generator to produce first n prime numbers.
A: We can create a generator function that yields prime numbers one by one until we reach the desired count.
'''

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def prime_generator(n):
    num = 2  # Start checking for prime numbers from 2
    while n:
        if is_prime(n):
            '''
            #yield keyword sed to retrun a value and then the code
            is resumed inside the function unlike the return keyword end
            the code when it is called
            # <yield> keyword is used to return a value and then the code
                '''
            yield num
            n -= 1
        num += 1 # Move to the next number

# Test case for generating first n prime numbers
n = int(input("Enter the number of prime numbers to generate: "))
for e in prime_generator(n):
    print(e, end=' ')