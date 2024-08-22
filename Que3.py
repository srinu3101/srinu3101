#Check whether the given number is positive and divisible by 5 or not.  
a = int(input("Enter the number:"))

if a > 0 and a%5 == 0:
    print("Number is positive snd divisible by 5")
elif a < 0 and a % 5 == 0:
    print("Number is Negative snd divisible by 5")
elif a > 0 and a %5 != 0:
    print("Number is positive snd not divisible by 5")
elif a < 0 and a % 5 != 0:
    print("Number is Negative snd not divisible by 5")

