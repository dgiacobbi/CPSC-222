# Programmer: David Giacobbi
# Class: CPSC 222-01, Spring 2022
# Data Assignment #2
# 2/10/22
# 
# Description: This program works with file I/O to perform calculations and format csv data for in-depth analysis.

import utils

def main():
    
    # Stores .csv data for further analysis
    apple_results = utils.read_data("apple_health_data.csv")

    # Define variables for the elements returned from read_data function
    apple_headers = apple_results[0]
    apple_data = apple_results[1]

    # Display the table in terminal
    utils.display_table(apple_headers, apple_data)
    print()

    # Prompt user for column to run statistical computations on
    apple_col_name = input("Please enter a column name to compute stats for: ")
    print()

    # Grab column based on input and perform stat analysis
    apple_col_data = utils.get_column(apple_headers, apple_col_name, apple_data)
    num_count = utils.num_count(apple_col_data)
    average = utils.compute_average(apple_col_data)
    std_deviation = utils.compute_std_deviation(apple_col_data)
    median = utils.compute_median(apple_col_data)
    smallest_num = utils.find_smallest_num(apple_col_data)
    largest_num = utils.find_largest_num(apple_col_data)

    # Display results to terminal
    print("Total Amount of Data Inputs:", num_count)
    print("Average of Data Inputs:", average)
    print("Standard Deviation of Column:", std_deviation)
    print("Median of Data Inputs:", median)
    print("Smallest Number in Column:", smallest_num)
    print("Largest Number in Column:", largest_num)
    print()

main()