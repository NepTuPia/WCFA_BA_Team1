import pandas as pd

lst = ["challenger_grandmaster_data.csv","master_diamond_data.csv", "diamond_emerald_data.csv", "emerald_platinum_data.csv", "gold_data.csv", "silver_data.csv"]

#lst = ["diamond_emerald_data.csv"]
# lst = ["combined_data.csv"]
for file_name in lst:
    # 데이터 불러오기
    path = "processed_raw_data/" + file_name
    data = pd.read_csv(path)

    data = data.dropna(axis=1)
    data = data.drop("champions", axis = 1)
    feature_name = data.columns


    # 'game_duration'을 초,중,후반으로 분류

    index = 0
    for i in feature_name:
        if i.split('_')[0] in ["TOP", "JUNGLE", "MIDDLE", "BOTTOM", "UTILITY"]:
            index += 1

    total_index = [feature_name[index], feature_name[len(feature_name)-1]]
    total_data = data.loc[:,total_index[0]:total_index[1]]

    bins = [0, 1200, 1800, float('inf')]
    labels = ['early', 'middle', 'final']
    data['game_duration_label'] = pd.cut(data['game_duration'], bins=bins, labels=labels, right=False)
    # print(data[['game_duration', 'game_duration_label']].head())
    print(data)
    data = data.drop('game_duration', axis=1)

    early_data = data[data['game_duration_label'] == 'early']
    middle_data = data[data['game_duration_label'] == 'middle']
    final_data = data[data['game_duration_label'] == 'final']

    duration_list = [early_data, middle_data, final_data]
    duration_labels = ['early', 'middle', 'final']

    tier = file_name.split('.csv')[0]
    tier = file_name.split('_data')[0]

    for duration_data, duration_label in zip(duration_list, duration_labels):
        duration_data.to_csv(f"processed_time_duration_data/{tier}_{duration_label}.csv", index=False)



