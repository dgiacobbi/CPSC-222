# Programmer: David Giacobbi
# Class: CPSC 222-01, Spring 2022
# Data Assignment #3
# 2/24/22
# 
# Description: This program takes in two csv files, provides stat analysis of the dataset, and joins the two csv files on "Date" column.

import pandas as pd

def main():

    # Load the two CSV files with date index
    youtube_df = load_csv_file("youtube_analytics_2-11-21_2-10-22.csv", "Date")
    days_df = load_csv_file("days_of_week_2-11-21_2-10-22.csv", "Date")

    # Prompt the user for a start/end date and slice youtube_df
    sliced_youtube_df = slice_user_df(youtube_df)

    # Display numeric column choices and prompt user for column name
    # .columns source: https://www.geeksforgeeks.org/get-list-of-column-headers-from-a-pandas-dataframe/
    print("\nNumeric Columns for Youtube Analytics\n")
    for i in range(len(sliced_youtube_df.columns)):
        print(sliced_youtube_df.columns[i])
    print()
  
    user_column_name = input("Please enter the name of a numeric column above to analyze: ")

    # Perform stat analysis and write results to new csv
    youtube_analysis_results = compute_df_analysis(sliced_youtube_df, user_column_name)
    youtube_analysis_results.to_csv("user_column_results.csv", header=False)

    # Perform outer join on date in youtube_df, write results to new csv
    merged_df = youtube_df.merge(days_df, on=["Date"], how="outer")
    merged_df.to_csv("merged_data.csv")

    # Split the data on the Day of Week, apply mean to user stat analysis column, combine all means into a series
    # Write results to a new csv
    daily_means_ser = split_apply_combine_df(merged_df, "Day of Week", user_column_name)
    daily_means_ser.to_csv("daily_means.csv", header=False)

def load_csv_file(csv_file, index):

    # Use pandas tool to read from csv and declare index
    csv_file_df = pd.read_csv(csv_file, index_col=index)

    # Parse through colon delimited data for Average view duration column to get numeric value
    # .columns source: https://www.geeksforgeeks.org/get-list-of-column-headers-from-a-pandas-dataframe/
    for i in range(len(csv_file_df.columns)):
        if csv_file_df.columns[i] == "Average view duration":       
            for line in range(len(csv_file_df)):

                values = csv_file_df.iloc[line, 5].split(":")
                values[0] = int(values[0]) * 3600
                values[1] = int(values[1]) * 60

                total_sec = values[0] + values[1] + int(values[2])
                csv_file_df.iloc[line, 5] = total_sec

    return csv_file_df

def slice_user_df(user_df):

    # Prompt user for the bounds needed to slice
    user_left_bound = input("Please enter a start date between 2/11/21 - 2/10/22: ")
    user_right_bound = input("Please enter an end date between 2/11/21 - 2/10/22: ")
    
    # Slice the inputed dataframe
    user_df = user_df[user_left_bound:user_right_bound]

    return user_df


def compute_df_analysis(data_df, column_name):
    
    # Create a Series from the user-entered column name and the sliced DataFrame
    user_analysis_ser = pd.Series(data_df[column_name])

    # Compute sum, mean, standard deviation, median, smallest value, and largest value on sliced column
    # Store these label/result pairs in a Pandas Series object.
    stat_headers = ["Sum", "Mean", "Standard Deviation", "Median", "Smallest Value", "Largest Value"]
    stat_data = [user_analysis_ser.sum(), user_analysis_ser.mean(), user_analysis_ser.std(), 
                 user_analysis_ser.median(), user_analysis_ser.min(), user_analysis_ser.max()]

    user_column_results = pd.Series(stat_data, index = stat_headers)

    return user_column_results

def split_apply_combine_df(analysis_df, split_attribute, column_name):

    # Split the inputed dataframe into subtables using specific attribute
    grouped_analysis_df = analysis_df.groupby(split_attribute)

    # Create a series to hold applied operation data for return
    mean_data_ser = pd.Series(dtype=float)

    # For loop computes mean of each split_attribute and writes it to series
    for group_name, group_df in grouped_analysis_df:
        group_mean_data = group_df[column_name].mean()
        mean_data_ser[group_name] = group_mean_data
    
    # Combined applied data is returned in this series
    return mean_data_ser

main()