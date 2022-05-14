# Programmer: David Giacobbi
# Class: CPSC 222-01, Spring 2022
# Data Assignment #4
# 3/14/22
# 
# Description: This program gives the stats of Xbox gamers from Call of Duty: Warzone, given their gamertag.

import requests
import json

# Using the Warzone API, prompt user for gamertag to use to get a json object
# To check program, my xbox gamertag is HUNCH0 PAPI
user_gamertag = input("Please enter your Warzone gamertag: ")

warzone_url = "https://call-of-duty-modern-warfare.p.rapidapi.com/warzone/"+str(user_gamertag)+"/xbl"

warzone_headers = {'x-rapidapi-key': "48c6248dd3msh5bf7b8a377bd25cp19e73ajsn114ccda534b5"}

warzone_response = requests.get(url=warzone_url, headers=warzone_headers)

# Parse through json object to collect dataset with player stats
warzone_json_obj = json.loads(warzone_response.text)
wz_br_all = warzone_json_obj["br_all"]

# Store each stat in a variable
wz_br_wins = wz_br_all["wins"]
wz_total_kills = wz_br_all["kills"]
wz_kd_ratio = round(wz_br_all["kdRatio"], 2)

# Convert time played to hours rather than seconds
wz_sec_played = wz_br_all["timePlayed"]
wz_hours_played = round(wz_sec_played / 3600, 2)

# Display results in organized format
print()
print("********* ", user_gamertag, " Warzone Stats *********", sep="")
print("Total Battle Royale Wins:", wz_br_wins)
print("Total Time Played (hours):", wz_hours_played)
print("Total Kills:", wz_total_kills)
print("Kill/Death Ratio:", wz_kd_ratio)
print()