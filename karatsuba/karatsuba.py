mult_table = {i:{j:i*j for j in range(10)} for i in range(10)}
# print(mult_table)

def karatsuba(x, y):
    global mult_table
    # Base case for recursion (single digits)
    if x < 10 and y < 10:
        return mult_table[x][y]

    # Calculate number of 0s
    m2 = max(len(str(x)), len(str(y))) // 2

    # Split the digit sequences in the middle 
    # divmod returns the div result (the first 1/2 of digits) and the remainder (the second 1/2)
    a, b = divmod(x, 10**m2)
    c, d = divmod(y, 10**m2)

    # 3 recursive calls for Karatsuba
    ones = karatsuba(b, d) 
    tens = karatsuba(a, c) # (a * 10^m2) * (c * 10^m2) = 
    cross = karatsuba((a + b), (c + d)) - (tens + ones) # 

    # Use the Karatsuba formula to combine the results
    return tens*10**(m2*2) + cross*10**m2 + ones

# Example usage
x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

result = karatsuba(x, y)

print(f"The result of multiplying {x} and {y} is \n{result}")
print(x*y)
