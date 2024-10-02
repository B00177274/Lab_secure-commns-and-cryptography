

#Program to find gcd(greatest common division)

def gcd(a, b):                                 #The function gcd(a, b) calculates the GCD of two numbers a and b.
    while b != 0:                              #It uses a while loop that continues as long as b is not zero.
        remainder = a % b
        a = b
        b = remainder
    return a                                    #In each iteration, the remainder of a % b is stored, and a is updated to b, while b is updated to the remainder.

                                                # Taking input from the user
                                                #Once b becomes zero, the loop exits, and a contains the GCD
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Calculate GCD
g = gcd(a, b)

# Print the result
print(f"The GCD of {a} and {b} is: {g}")
