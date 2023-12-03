import csv
import json
import os
import time
import requests

import csv_functions
import riot_api_function

api_key = 'RGAPI-5f59d95b-ab8a-421f-8488-35c9a20628a9'
headers = {"X-Riot-Token": api_key}
challenger_gm = "스트레스유발협곡"
diamond = "역시남자라면"
emerald_platinum = "멀 째려"
gold = "EDM은 못참지"
silver = "달수빈"

total_matchid_list = []
total_puuid_list = []

start_puuid = riot_api_function.check_summoner_exists(diamond)
total_puuid_list.append(start_puuid)
puuid_idx = 0
while len(total_matchid_list) < 4500:
    match_ids = riot_api_function.get_recent_match(total_puuid_list[puuid_idx])
    puuid_idx += 1
    extened_length = 0
    for match_id in match_ids:
        if match_id not in total_matchid_list:
            total_matchid_list.append(match_id)
            extened_length += 1
    print(len(total_matchid_list))
    print(len(total_matchid_list) - extened_length)
    try:
        match_data = riot_api_function.get_match_data(total_matchid_list[len(total_matchid_list)-extened_length])
    except:
        print("---------------------------------------------------------")
        print(len(total_matchid_list))
        print(len(total_matchid_list) - extened_length)
        print("---------------------------------------------------------")
    puuid_list = match_data['metadata']['participants']
    for puuid in puuid_list:
        if puuid not in total_puuid_list:
            total_puuid_list.append(puuid)
    time.sleep(2)

print(total_matchid_list)
csv_functions.save_to_csv(total_matchid_list, 'silver_matchid.csv')
csv_functions.save_to_csv(total_puuid_list, 'silver_puuid.csv')