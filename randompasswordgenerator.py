import random as rd
# random password generator this is no doubt my first project which i built with my own skills
mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '@', '$', '#', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
length = len(mylist) - 1

password = mylist[rd.randint(0, length)]
for x in range(7):
    password += mylist[rd.randint(0, length)]

print(f"your password is : {password}")
