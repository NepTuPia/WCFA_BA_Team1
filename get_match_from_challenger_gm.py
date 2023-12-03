import csv
import time
import requests

import csv_functions
import riot_api_function

total_matchid_list = csv_functions.read_first_column('real_challenger_matchid.csv')
total_puuid_list = csv_functions.read_second_column('real_challenger_puuid.csv')

for puuid in total_puuid_list:
    match_ids = riot_api_function.get_recent_match(puuid)
    for match_id in match_ids:
        if match_id not in total_matchid_list:
            print("successfully saved info of", match_id)
            total_matchid_list.append(match_id)
            csv_functions.append_to_csv('real_challenger_matchid.csv', [match_id])
        else:
            print("Already saved info of", match_id)
            continue
    print(len(total_matchid_list))
    time.sleep(2)