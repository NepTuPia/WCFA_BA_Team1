import csv
def save_to_csv(data, filename):
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
        print(f"Data successfully saved to {filename}.")
    except Exception as e:
        print(f"Error while saving the data: {e}")
def open_csv(filename):
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            data.append(row)
        return data[0]

matchid_1 = open_csv("matchid_and_puuid_ver2/gold_matchid_unduplicated.csv")

matchid_2 = open_csv("matchid_and_puuid_ver2/silver_matchid.csv")

dct = {}

not_duplication_list = []

for match_id in matchid_1:
    if dct.get(match_id) is None:
        dct[match_id] = 1
    else:
        print("Exists already in initial data")

for match_id in matchid_2:
    if dct.get(match_id) != None:
        print("Duplication find!")
    else:
        not_duplication_list.append(match_id)
print(len(matchid_2))
save_to_csv(not_duplication_list, "matchid_and_puuid_ver2/silver_matchid_unduplicated.csv")
print(len(not_duplication_list))