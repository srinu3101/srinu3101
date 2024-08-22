#write a program to store seven fruits in a list entered by the user
fruits = []
for i in range(7):
    fruit = input(f"enter the fruits name {i+1}:")
    fruits.append(fruit)
print("the list of fruits enterd is:", fruits)

