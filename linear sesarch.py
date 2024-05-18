# create a list of numbers
limit = int(input("Enter a Limit : "))
number_list = []
for i in range(limit):
    number = int(input(f"Enter the {i} Number : "))
    number_list.append(number)

print(f"Number list is : {number_list}")

x=int(input("enter a number to serach : "))
f=0

# Searching a target in linear format
for index in range(len(number_list)):
    if number_list[index]==x:
        print("element found at : ",index)
        f = 1
        break
if f==0:
    print("element not found")