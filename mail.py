def add_func(n1 , n2):
    return n1 + n2

def sub_func(n1 , n2):
    return n1 - n2

def x_func(n1 , n2):
    return n1 * n2

def divide_func(n1 , n2):
    return n1 / n2

def pow_func(n1 , n2):
    return n1 ** n2


num1,num2, res = 100, 200, 0



res = add_func(num1,num2)
print(f"{num1} + {num2} = {res}" )




res = sub_func(num1,num2)
print(f"{num1} - {num2} = {res}" )






res = x_func(num1,num2)
print(f"{num1} * {num2} = {res}" )




res = divide_func(num1,num2)
print(f"{num1} / {num2} = {res}" )



res = pow_func(num1,num2)
print(f"{num1} ** {num2} = {res}" )


