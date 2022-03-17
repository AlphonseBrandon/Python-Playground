# Author : Alphonse Brandon
# Date : 14 March 2022
# Time : 11:03pm

# Reviewing the "for loop" basic syntax

for x in range(6):
    print(x)
else:
    print("Range exhausted!")


# loop through a list

fruits = ["Apple", "Spice", "Tomato"]

for fruit in enumerate(fruits):
    print(fruit)

# Referencing the index

for i, fruitt in enumerate(fruits):
    print("Index:", i, "fruit:", fruitt)