#my_list = [17,3,11,5,1,9,7,15,13]
my_list = []
largest = 0

for num in range(5):
   number = int(input("Enter a number: "))
   my_list.append(number)

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print("The greater value is: ", str(largest))