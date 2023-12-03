import csv
import json
import os
import time
import requests

import json_functions
import riot_api_function

match_ids = []

with open('real_challenger_matchid.csv', 'r') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        match_ids.append(row)

cnt = 0
for match_id in match_ids:
    match_id = match_id[0]
    cnt += 1
    print(cnt)
    filename = match_id + ".json"
    path = "real_challenger_data/"
    if not os.path.exists(path + filename):
        match_data = riot_api_function.get_match_data(match_id)
        json_functions.save_dict_from_json("real_challenger_data/" + match_id + ".json", match_data)
        print("Successfuly save", filename)
        time.sleep(1)
    else:
        print("Already Exists in file:", filename)