# 1) Write a recursive function to print N natural numbers.

def printN(n):
    if n>0:
        printN(n-1)
        print(n)
printN(20) 

# 2)Write a recursive function to print N natural numbers in reverse order.

def printrev(n):
    if n>0:
        print(n)
        printrev(n-1)
printrev(20) 

# 3) Write a recursive function to print first  N odd natural numbers.

def printodd(n):
    if n>0:
        printodd(n-1)
        print(2*n-1)
        
printodd(10)        

# 4) Write a recursive function to print first N even natural numbers.

def printeven(n):
    if n>0:
        printeven(n-1)
        print(2*n)
        
printeven(10)  

# 5) Write a recursive function to print first  N odd natural numbers in reverse order.

def printodd(n):
    if n>0:
        print(2*n-1)
        printodd(n-1)
        
        
printodd(10)

# 6) Write a recursive function to print first  N even natural numbers in reverse order.

def printeven(n):
    if n>0:
        print(2*n)
        printeven(n-1)
        
        
printeven(10) 

# 7) Write a recursive function to calculate sum of first N natural numbers.

def firstN(n):
    if n==1:
        return 1
    return n+firstN(n-1)
print("Sum of first 5 natural no:", firstN(5))

# 8) Write a recursive function to calculate sum of first N odd natural numbers.

def firstodd(n):
    if n==1:
        return 1
    return (2*n-1)+firstodd(n-1)
print(firstodd(5))

# 8) Write a recursive function to calculate sum of first N even natural numbers.

def firsteven(n):
    if n==1:
        return 2
    return (2*n)+firsteven(n-1)
print(firsteven(5))

# 8) Write a recursive function to calculate factorial of a number.

def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print(fact(5))

# 8) Write a recursive function to calculate sum of squares of first N natural numbers.

def sum_sq(n):
    if n==1 :
        return 1
    return n*n+sum_sq(n-1)
print(sum_sq(5))

