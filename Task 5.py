# 1. Write a program to calculate total number of vowels

data = input("Enter the string:")
vowel_list = []
consonants = []
def count_vowel():
    vowels = ['a','e','i','o','u']
    for char in data:
        if char in vowels:
            vowel_list.append(char)
        else:
            consonants.append(char)


count_vowel()
print("The string count of vowels is:","".join(vowel_list))
print(len(vowel_list))


# 2. Write a pyramid of numbers 1 to 20 using For loop
levels = int(input("Enter number of rows: "))

for i in range(levels):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\n")


# 3. Write a function that takes a string and returns a new string with all the vowels removed.
data = input("Enter the string:")

vowel_list = []
consonants = []

def alphabets():
    vowels = ['a', 'e', 'i', 'o', 'u']

    for char in data:
        if char in vowels:
            vowel_list.append(char)
        else:
            consonants.append(char)



alphabets()
print("String without vowels is :", "".join(consonants))




# 4. Write a function that takes a string and returns unique characters in it.

data = input("Enter the string:")
unique_list=[]

def unique():
    for char in data:
        if char not in unique_list:
            unique_list.append(char)


unique()
print("The string is:","".join(unique_list))




# 5. Write a function that takes a string and returns True if Palindrome and False otherwise.
def is_palindrome(input_string):
    reversed_string = input_string[::-1]
    return input_string == reversed_string

data = input("Enter the string: ")

if is_palindrome(data):
    print("True")
else:
    print("False")



# 6. Write a function that takes two string and returns the longest common substring between them.

def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)

    table = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0
    end_index = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
                if table[i][j] > max_length:
                    max_length = table[i][j]
                    end_index = i

    longest_common_sub = str1[end_index - max_length: end_index]
    return longest_common_sub

data1 = input("Enter the first string: ")
data2 = input("Enter the second string: ")

result = longest_common_substring(data1, data2)
print("The longest common substring is:", result)

# 7. Write a function that takes string and returns most frequently used character in it.
data = input("Enter the string:")
list1 = []
frequent_list = []

def frequent_character():

    for char in data:
        if char in list1:
            frequent_list.append(char)
        else:
            list1.append(char)

frequent_character()
print("Frequently used character is :",(frequent_list))

# 8. Write a function that takes a string and returns true if it is anagram of another string ,otherwise false.
from collections import Counter
def are_anagrams(str1, str2):
    return Counter(str1) == Counter(str2)

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")


# 9. Write a function that takes a string and returns total number of words in it.
def num_of_words(input):
    x = input.split()
    return len(x)


input = input("Enter the first string: ")

total_words =num_of_words(input)
print("The total number of words :",(total_words))










