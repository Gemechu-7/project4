#write a programme to remove the duplicate a list
# By using while loop
numbers =[2, 3, 4, 4, 5, 7, 7 ,7 , 8, 6, 9, 10 , 11, 11]
unique_numbers = []
count = 0
while count < len(numbers):
  if numbers[count] not in unique_numbers:
    unique_numbers.append(numbers[count])
  count+=1
print(unique_numbers)