Age = int(input("enter the age"))
Gender = str(input("enter the gender"))
if Age >60 and Gender =='male':
    print(" 70% of fare is applicable ")
elif Age>60 and Gender == 'female':
    print(" 50% of fare is applicable")
elif (Age >10 and Age <60) and Gender == 'female':
    print(" 70% of fare is applicable")
elif (Age >10 and Age <60) and Gender == 'male':
    print(" 100% of fare is applicable")
    
