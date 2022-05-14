# Programmer: David Giacobbi
# Class: CPSC 222-01, Spring 2022
# Data Assignment #2
# 2/10/22
# 
# Description: This program works with file I/O to perform calculations and format csv data for in-depth analysis.

import utils

def main():

    # Stores .csv data for further analysis
    fitbit_results = utils.read_data("fitbit_data.csv")
    
    # Define variables for the elements returned from read_data function
    fitbit_headers = fitbit_results[0]
    fitbit_data = fitbit_results[1]

    # Display the table in terminal
    utils.display_table(fitbit_headers, fitbit_data)
    print()

    # Prompt user for column to run statistical computations on
    fitbit_col_name = input("Please enter a column name to compute stats for: ")
    print()

    # Grab column based on input and perform stat analysis
    fitbit_col_data = utils.get_column(fitbit_headers, fitbit_col_name, fitbit_data)
    num_count = utils.num_count(fitbit_col_data)
    average = utils.compute_average(fitbit_col_data)
    std_deviation = utils.compute_std_deviation(fitbit_col_data)
    median = utils.compute_median(fitbit_col_data)
    smallest_num = utils.find_smallest_num(fitbit_col_data)
    largest_num = utils.find_largest_num(fitbit_col_data)

    # Display results to terminal
    print("Total Amount of Data Inputs:", num_count)
    print("Average of Data Inputs:", average)
    print("Standard Deviation of Column:", std_deviation)
    print("Median of Data Inputs:", median)
    print("Smallest Number in Column:", smallest_num)
    print("Largest Number in Column:", largest_num)
    print()

main()