#How do we create a sequence of numbers in Python?
A = range (10)
print(list(A))

#Read the input from keyboard and print a sequence of numbers up to that number
n = int(input("enter the value"))
for i in range(n):
    print(i)