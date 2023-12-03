import json
import os

import json_functions

path = "processed_data/"
tier_path = "silver_data/"

files = os.listdir(path + tier_path)

entire_data = ""
flag = 0
for file in files:
    if file == ".DS_Store":
        continue
    crt_data = json_functions.open_json(path + tier_path + file)
    if flag == 0:
        flag += 1
        for key in crt_data:
            for inner_key in crt_data[key]:
                entire_data += inner_key + ','
        entire_data += '\n'
    for key in crt_data:
        for inner_key in crt_data[key]:
            if inner_key == "champions":
                strr = ''
                for champion in crt_data[key][inner_key]:
                    strr += champion + ' '
                strr += ','
                entire_data += strr
            else:
                entire_data += str(crt_data[key][inner_key]) + ','
    entire_data += '\n'
with open("processed_raw_data/silver_data.csv", 'w') as file:
    file.write(entire_data)