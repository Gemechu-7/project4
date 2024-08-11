#Write a program change number in a digit to words, by using for loop and dictionary
numbers = input('numbers: ')
numbers_words={
  # '0':'zero ',
  '1': 'one ',
  '2': 'two ',
  '3': 'three ',
  '4': 'four ',
  '5': 'five ',
  '6': 'six ',
  '7': 'seven ',
  '8': 'eight ',
  '9': 'nine '
}
output = ''
for char in numbers:
  output+=numbers_words.get(char, "plus ")
print(output)
#the question using while loop and dictionary
phone_numbers = input('phone: ')
phone_words = {
 # '0':'zero ',
  '1': 'one ',
  '2': 'two ',
  '3': 'three ',
  '4': 'four ',
  '5': 'five ',
  '6': 'six ',
  '7': 'seven ',
  '8': 'eight ',
  '9': 'nine ' 
}
words_output = ""
count = 0
while count < len(phone_numbers):
  words_output+= phone_words.get(phone_numbers[count], "plus ")
  count+=1
print(words_output)