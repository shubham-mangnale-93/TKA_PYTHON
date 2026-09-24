'''
#For Loop : 
For loops is used to iterate over a sequence such as a list, tuple, string or range. 
It executes a block of code once for each item in the sequence.
A for loop is used to repeat a block of code for each item in a sequence.
Syntax :
   for var in Iterable:
          #body|block to execute
          #code|logic
'''
#--------------------------------------------------------------------------------------------

numbers = [1,2,3,4]
print("Start")
for num in numbers:
    print(num)
    # print("Hello")
print("THE END")    


n = 4
for i in range(0,n):
    print(i)


# def count_digits(s):
#     count = 0
#     for ch in s:
#         if ch.isdigit():
#             count += 1
#     return count

# text = input("Enter a word/sentence: ")
# print("Count of digits:", count_digits(text))


def count_chars_in_range(s, start, end):
    count = 0
    for ch in s:
        if start <= ch <= end:
            count += 1
    return count

text = input("Enter string: ")
result = count_chars_in_range(text, 'a', 'p')
print("Count of characters between a-p:", result)