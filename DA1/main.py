# Programmer: David Giacobbi
# Class: CPSC 222-01, Spring 2022
# Data Assignment #1
# 1/23/22
# I attempted the bonus.
# 
# Description: This program sorts a list of floats in descending order and computes a variety of calculations for data analytics. It 
#              also modifies the list using user input.

gonzaga_stats = [13.1, 1.7, 1.8, 7.8, 1.2, 12.9, 10.6, 5.8, 3.0, 9.7, 18.6, 0.5, 7.6, 0.1]

# List sort in descending order
gonzaga_stats.sort()
gonzaga_stats.reverse()
print(gonzaga_stats)

# Count Computation
count = len(gonzaga_stats)
print("Count:", round(count, 2))

# Mean/Average Computation
total = 0

# Finding the sum of all the stats in list
for stat in gonzaga_stats:
    total += stat

average = total / count
print("Average:", round(average, 2))

# Median Computation
median = (gonzaga_stats[6] + gonzaga_stats[7]) / 2
print("Median:", round(median, 2))

# Smallest Number Computation
min_num = gonzaga_stats[0]

# For loop goes through each list element, comparing its value to the current lowest value
for stat in gonzaga_stats:
    if stat <= min_num:
        min_num = stat

print("Smallest Number:", round(min_num, 2))

# Largest Number Computation
maxNum = -1

# For loop goes through each list element, comparing its value to the current highest value
for stat in gonzaga_stats:
    if stat >= maxNum:
        maxNum = stat

print("Largest Number:", round(maxNum, 2))

# Prompt User for Index and New Value
user_index = input("Please enter an index to modify: ")
user_value = input("Please enter a new value for this index: ")

gonzaga_stats[int(user_index)] = user_value

print(gonzaga_stats)

# Bonus Task: Displaying List with ~
i = 0
while i < len(gonzaga_stats):

    if i < len(gonzaga_stats) - 1:
        print(gonzaga_stats[i], end = " ~ ")
    else:
        print(gonzaga_stats[i], end = "")

    i += 1