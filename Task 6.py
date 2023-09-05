# 1. You have been given a Python list ,your task is to create two list one list even nos and other with odd nos.
Given_list =[10,501,22,37,100,999,87,351]
even_list=[]
odd_list=[]

def even_odd():

    for n in Given_list:
        if n % 2 == 0:
            even_list.append(n)
        else:
            odd_list.append(n)

even_odd()
print("The Even numbers are :",(even_list))
print("The odd numbers are:",(odd_list))

#2. You have been given a Python list ,your task is to Count all the Prime nos and create a new list which contains all the Prime nos.

Given_list =[10,501,22,37,100,999,87,351]
Prime_nos = []

def is_prime(num):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    return False

def Prime():
    for n in Given_list:
        if is_prime(n):
            Prime_nos.append(n)

Prime()
print("The Prime numbers:", Prime_nos)

# 3. Write a Python program to find how many numbers in the given list are happy numbers.
Given_list =[10,501,22,37,100,999,87,351]
Happy_nos = []

def is_happy_number(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1

def happy_nos():
    for n in Given_list:
        if is_happy_number(n):
            Happy_nos.append(n)

happy_nos()
print("The Happy numbers:", Happy_nos)

# 4. Write a program to find the sum of first and last digit of the interger.

# We have a number
number = input("Enter the number:")

# We are type casting it in string
number = str(number)

# Storing first and last digit in a variable
# after type casting into Integer.
first_digit = int(number[0])
last_digit = int(number[-1])

# Adding these two variables
addition = first_digit + last_digit

# Display our output
print('Addition of first and last digit of the number is',addition)


#5. You have been given a list of N integers which represents the number of mangoes in a bag.Each bag has a variable number of mangoes.There are M students, your task is to distribute mangoes in such a way that each gets one bag.
# The difference between number of mangoes in a bag with maximum mangoes and bag with minimum mangoes given to the student is minimum


def minimize_difference(mangoes, students):
    mangoes.sort()  # Sort the mangoes list in ascending order
    min_difference = float('inf')  # Initialize with a very large value

    left, right = 0, len(mangoes) - 1

    while right >= left:
        difference = mangoes[right] - mangoes[left]
        min_difference = min(min_difference, difference)

        left += 1
        right -= 1

    return min_difference


# Example inputs
mangoes_in_bags = [7, 3, 2, 4, 9, 1]
num_students = 3

result = minimize_difference(mangoes_in_bags, num_students)
print("Minimum difference:", result)


# 6. You have been given three lists.You task is to find the duplicates in the three list.Write the program for the same.You can use your own list
list1 =['pink','cycle','bus','boat']
list2 = ['pink','bus','red','blue']
list3 = ['blue','train','boat','aeroplane']
duplicate=[]

for data in list1:
     if data in list2:
            duplicate.append(data)

for data in list2:
     if data in list3:
         duplicate.append(data)

for data in list3:
     if data in list1:
         duplicate.append(data)

print("The duplicate items are:",(duplicate))



# 7. Write a python program to find the first no repeating elements in a given list of intergers.
list1 =['5','2','1','4','2','5','6']
repeat=[]
non_repeat=[]

for data in list1:
    if list1.count(data) > 1:
        repeat.append(data)
    else:
        non_repeat.append(data)

print("The non repeating numbers are:",(non_repeat))
print("The First non-repeating number is:",(non_repeat[0]))


# 8. Write a python program to find the minimum element in the rated and sorted list.

list1 =['8','2','1','0','2','9','6']

list1.sort()    # The list is sorted
print("The sorted list:",(list1))
x = min(list1)
print("The minimum element in sorted list is:",(x))


# 9. You have been given a python list [10,20,30,9] and a value of 59.Write a program to find a triplet in the list whose sum is equal to the given value.9
given_list = [10, 20, 30, 9]
given_value = 59

# Iterate through all possible combinations of three numbers from the list
for i in range(len(given_list)):
    for j in range(i + 1, len(given_list)):
        for k in range(j + 1, len(given_list)):
            if given_list[i] + given_list[j] + given_list[k] == given_value:
                print("Triplet found:", given_list[i], given_list[j], given_list[k])
                break



# 10. Given a list ,write a program to find if there is a sublist with sum equal to zero
def has_sublist_with_zero_sum(lst):
    prefix_sum = 0
    seen_prefix_sums = set()

    for num in lst:
        prefix_sum += num

        if prefix_sum == 0 or prefix_sum in seen_prefix_sums:
            return True

        seen_prefix_sums.add(prefix_sum)

    return False

given_list = [4, 2, -3, 1, 6]
result = has_sublist_with_zero_sum(given_list)

if result:
    print("There is a sublist with a sum equal to zero.")
else:
    print("There is no sublist with a sum equal to zero.")


