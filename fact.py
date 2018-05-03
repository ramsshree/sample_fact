
n = input("Enter the number: ")

fact = 1
if n == 0 or n==1:
    return fact
for i in range(2,n+1):
    fact = fact * i
return fact
    
