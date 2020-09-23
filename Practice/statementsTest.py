# st = 'Print only the words that start with s in this sentence'

 # print(st.split()[0][0])


# for word in st.split():
#     if word.split()[0][0].lower() == 's':
#         print(word)


# Use range() to print all the even numbers from 0 to 10.

# x = range(0,11,2)
# for number in x:
#     print(number)

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

# numbers = [ number for number in range(0,51) if number % 3 == 0]
# print(numbers)



# Go through the string below and if the length of a word is even print "even!"

# st = 'Print every word in this sentence that has an even number of letters'

# even_length_words = [word for word in st.split() if len(word) % 2 == 0]
# print(even_length_words)

# Write a program that prints the integers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".

# Multiples of 3 print "Fizz"
# Multiples of 5 print "Buzz"
# Multiples of 3 and 5 print "FizzBuzz"

# for num in range(0,101):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)


# Use List Comprehension to create a list of the first letters of every word in the string below:

# st = 'Create a list of the first letters of every word in this string'

# firstLetter = [letter[0] for letter in st.split()]
# print(firstLetter)

