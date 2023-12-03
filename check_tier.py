import os
import time
import csv_functions
import json_functions
import riot_api_function

tier_weight = {
    "CHALLENGER" : 10,
    "GRANDMASTER" : 9,
    "MASTER" : 8,
    "DIAMOND" : 7,
    "EMERALD" : 6,
    "PLATINUM" : 5,
    "GOLD" : 4,
    "SILVER" : 3,
    "BRONZE" : 2,
    "IRON" : 1,
}

path = "master_diamond_data/"
result_path = "check_lists/master_diamond_checklist.csv"
checked_list = csv_functions.read_first_column(result_path)
files = os.listdir(path)

for file in files:
    try:
        if file in checked_list:
            print("Already checked!:", file)
            continue
        data = json_functions.open_json(path + file)
        participants = data["metadata"]["participants"]
        match_tier_list = []
        match_average_tier = 0
        count = 0
        for participant in participants:
            id = riot_api_function.check_summoner_by_puuid(participant)
            tier = riot_api_function.check_summoner_league_by_id(id)
            match_tier_list.append(tier)
            match_average_tier += tier_weight[tier]
            count += 1
        if count == 0:
            continue
        match_average_tier /= count
        print(match_average_tier)
    except Exception as e:
        print("Some error in " + file)
        print(e)
        time.sleep(20)
        continue
    csv_functions.append_to_csv(result_path, [file, match_average_tier, match_tier_list])
    checked_list.append(file)
    time.sleep(20)


