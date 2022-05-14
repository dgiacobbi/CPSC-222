# Programmer: David Giacobbi
# Class: CPSC 222-01, Spring 2022
# Data Assignment #4
# 3/14/22
# 
# Description: This program uses APIs to create a cleaned data frame of a city's daily weather from the past year.

import requests
import json
import pandas as pd

def main():

    # Prompts user for large city and replaces spaces with +
    user_city = input("Please enter the name of a large city: ")
    user_city = user_city.replace(" ", "+")

    # Find latitude and longitude of city and store in variables
    city_coordinates = find_lat_long(user_city)
    city_latitude = city_coordinates[0]
    city_longitude = city_coordinates[1]

    # Use longitude and latitude to find the closest weather station for MeteoStatAPI
    city_station_id = get_weather_station(city_latitude, city_longitude)

    # Use the station id to get the weather data for the past year
    city_weather_df = get_weather_data(city_station_id)

    # Clean any missing values in the weather dataframe
    city_weather_df = clean_weather_df(city_weather_df)
    print(city_weather_df)

    # Write the cleaned data frame to a csv file
    user_city = user_city.replace("+", "_")
    city_weather_df.to_csv(str(user_city)+"_daily_weather_cleaned.csv")

def find_lat_long(user_city):

    # Using MapQuestAPI, create a json object that contains the coordinates for user_city
    mapquest_url = "http://www.mapquestapi.com/geocoding/v1/address"

    mapquest_key = "uHwDigrWGqFJdAvq0DsGYnhdUdJwJLlL"

    mapquest_query = {"key": mapquest_key, "location": user_city}

    mapquest_response = requests.get(url=mapquest_url, params=mapquest_query)

    # Parse through the json object to find the latitude and longitude for user_city
    mq_json_obj = json.loads(mapquest_response.text)
    mq_results = mq_json_obj["results"]
    mq_result = mq_results[0]
    mq_locations = mq_result["locations"]
    mq_locations = mq_locations[0]
    mq_lat_lng = mq_locations["latLng"]

    # Assign json data to variables for return
    latitude = mq_lat_lng["lat"]
    longitude = mq_lat_lng["lng"]

    return latitude, longitude

def get_weather_station(latitude, longitude):

    # Using the MeteoStatAPI, use the coordinates from user_city to produce new json object
    station_url = "https://meteostat.p.rapidapi.com/stations/nearby"

    station_key = "48c6248dd3msh5bf7b8a377bd25cp19e73ajsn114ccda534b5"
    station_headers = {"x-rapidapi-key": station_key}
    station_query = {"lat": latitude, "lon": longitude}

    station_response = requests.get(url=station_url, headers=station_headers, params=station_query)

    # Parse through json object to store closest station id in variable for return
    station_json_obj = json.loads(station_response.text)
    station_data = station_json_obj["data"]
    station_close = station_data[0]
    station_id = station_close["id"]

    return station_id

def celsius_to_fahrenheit(daily_weather_df, column):

    # For loop converts each celsius temp in a certain column to fahrenheit
    for day in range(len(daily_weather_df[column])):

        celsius_temp = daily_weather_df.loc[day, column]
        fahr_temp = (celsius_temp * (9/5)) + 32
        fahr_temp = round(fahr_temp, 2)
        
        daily_weather_df.loc[day, column] = fahr_temp


def get_weather_data(station_id):
    # Using MeteoStatAPI, get the weather data for the past year in user_city with station id
    weather_url = "https://meteostat.p.rapidapi.com/stations/daily"

    weather_key = "48c6248dd3msh5bf7b8a377bd25cp19e73ajsn114ccda534b5"
    weather_headers = {"x-rapidapi-key": weather_key}
    weather_query = {"station": station_id, "start": "2021-02-21", "end": "2022-02-20"}

    weather_response = requests.get(url=weather_url, headers=weather_headers, params=weather_query)

    # Parse through json object and storel data in dataframe for return
    weather_json_obj = json.loads(weather_response.text)
    weather_data_list = weather_json_obj["data"]

    daily_weather_df = pd.DataFrame(weather_data_list)

    # Set the units to be imperial to get Fahrenheit instead of Celsius
    celsius_to_fahrenheit(daily_weather_df, "tavg")
    celsius_to_fahrenheit(daily_weather_df, "tmin")
    celsius_to_fahrenheit(daily_weather_df, "tmax")

    return daily_weather_df

def clean_weather_df(daily_weather_df):

    # Check each of the columns in dataframe, and delete any with more than half missing values
    del_col_count = 0

    # For loop checks each column series for missing values
    for i in range(len(daily_weather_df.columns)):

        index = i - del_col_count

        col_index = daily_weather_df.columns[index]
        column_length = len(daily_weather_df[col_index])
        col_null_count = daily_weather_df[col_index].isnull().sum()

        if col_null_count > (column_length / 2):
            # Solution used for removing a column from Pandas dataframe
            # https://stackoverflow.com/questions/13411544/delete-a-column-from-a-pandas-dataframe
            daily_weather_df = daily_weather_df.drop(col_index, axis=1)
            del_col_count += 1

    # For loop checks and fills any other missing values in the remaining columns
    for i in range(len(daily_weather_df.columns)):

        col_index = daily_weather_df.columns[i]
        column_length = len(daily_weather_df[col_index])
        col_null_count = daily_weather_df[col_index].isnull().sum()
        
        if col_null_count > 0:

            # Interpolation used for any middle values
            daily_weather_df[col_index].interpolate(method="linear", limit_direction="forward", inplace=True)

            # If the last value is missing, forward fill na
            if daily_weather_df.iloc[column_length - 1, i] == None:
                daily_weather_df[col_index].fillna(method="ffill", inplace=True)
            
            # If the first value is missing, back fill na
            elif daily_weather_df.iloc[0, i] == None:
                daily_weather_df[col_index].fillna(method="bfill", inplace=True)

    return daily_weather_df

main()