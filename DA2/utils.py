# Programmer: David Giacobbi
# Class: CPSC 222-01, Spring 2022
# Data Assignment #2
# 2/10/22
# 
# Description: These utility function are used to display the file and perform stat calculations.

import math

# Opens filename for reading and loads the column names into a 1D list called headers and loads the data into a 2D list called data
def read_data(filename):
    infile = open(filename, "r")

    # Stores header line and clean up whitespace
    headers = infile.readline()
    headers.strip()

    # Takes in each line of data and stores each row of data in a table, clean up whitespace
    data = infile.readlines()
    for i in range(len(data)):
        data[i] = data[i].strip()
    
    return headers, data

# Displays the header row and the data in a grid-like table format
def display_table(headers, data):
    
    table = []

    # Divides headers indicies by string instead of character
    headers = headers.split(",")

    # For loop takes in a line of data and divides its indicies by string instead of character
    # Adds to table for printing
    for line in data:
        values = line.split(",")
        table.append(values)
    
    # For loop pares down and spaces out header titles for better visual display
    for i in range(len(headers)):
        group_string = headers[i]
        print(group_string[0:9], end = "\t      ")
    print()

    # For loop prints out each element in the table, spacing out each data input for organized formatting
    for i in range(len(table)):
        for value in table[i]:
            print(value, end = "\t\t")
        print()

# Returns a 1D list representing the column named col_name in data
def get_column(headers, col_name, data):

    data_table = []
    col_data = []

    # Divides headers indicies by string and cleans up any whitespace or newlines
    header_names = headers.split(",")
    for i in range(len(header_names)):
        header_names[i] = header_names[i].strip()

    # Finds the index of the column name that the user picks in main.py
    col_index = header_names.index(col_name)
    
    # For loop takes in a line of data and divides its indicies by string instead of character
    # Adds to table for column sorting
    for line in data:
        values = line.split(",")
        data_table.append(values)
    
    # For loop adds data inputs only from user requested column to 1-D list, col_data
    for row in range(len(data_table)):
        col_data.append(float(data_table[row][col_index]))

    return col_data

# Count of the numbers
def num_count(col_data):

    # Number count is same as the length of column data points
    count = len(col_data)
    return count

# Average (mean) of the numbers
def compute_average(col_data):

    # Sum function adds all data inputs in list and divides by its length
    average = sum(col_data) / len(col_data)
    average = round(average, 2)
    return average

# Standard deviation of the numbers
def compute_std_deviation(col_data):

    # Find the average of the data set first
    average = sum(col_data) / len(col_data)

    # Stores the increasing sum of the square of each point minus the average
    sum_of_sq_difference = 0

    # For loop finds the total sum of square differences between points and average
    for i in range(len(col_data)):
        sq_difference = math.pow((col_data[i] - average), 2)
        sum_of_sq_difference += sq_difference
    
    # Calculates and rounds last part of standard deviation using square root function from math module
    std_deviation = math.sqrt(sum_of_sq_difference / len(col_data))
    std_deviation = round(std_deviation, 2)
    return std_deviation


# Median number
def compute_median(col_data):

    # Sort the column list from smallest to greatest
    col_data.sort()

    # If statement determines if col_data has an exact middle
    if len(col_data) % 2 != 0:
        median_index = len(col_data) / 2
        median_index = round(median_index, None)
        median = col_data[median_index]
    # No exact middle means the two middle data points need to be averaged
    else:
        median_index = len(col_data) / 2
        median_index = round(median_index, None)
        median = (col_data[median_index] + col_data[median_index]) / 2
    
    median = round(median, 2)
    return median

# Smallest number
def find_smallest_num(col_data):

    # Smallest number starts at first data point, but can change through list sorting
    min_num = col_data[0]

    # For loop compares current smallest number to all other values in list
    for i in range(len(col_data)):
        if col_data[i] <= min_num:
            min_num = col_data[i]

    min_num = round(min_num, 2)
    return min_num

# Largest number
def find_largest_num(col_data):

    # Largest number starts at first data point, but can change during list sorting
    max_num = col_data[0]

    # For loop compares current largest number to all other values in list
    for i in range(len(col_data)):
        if col_data[i] >= max_num:
            max_num = col_data[i]
    
    max_num = round(max_num, 2)
    return max_num