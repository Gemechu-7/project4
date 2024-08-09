#write a programme to remove the duplicate a list
# By using for loop
numbers =[2, 3, 4, 4, 5, 7, 7 ,7 , 8, 6, 9, 10 , 11, 11]
unique_number = []
for count in numbers:
  if count not in unique_number:
    unique_number.append(count)
print(unique_number)