# Hence in this file we will learn about the loops
# In this we will learn about the for loop and while loop
# And doing the practice of it

# Let's Practice the loops:

# Practice of the while loop:

# #Print Numbers from 1 to 100:

# i = 1
# while i <= 100:
   
#    print(i)
#    i+= 1

# #Print numbera 100 to 1.

# a = 100
# while a >= 1:
#     print(a)
#     a-= 1

# #Print the multiplication table of a number entered by the user.

# num = int(input("Enter a number: "))  
# i = 1
# while i <= 10:
#     print(num * i)
#     i+= 1

#Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 

my_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

i = 0
while i <= 10:
    print(my_list[i])
    i+= 1
