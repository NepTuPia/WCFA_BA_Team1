import pandas as pd

tier_lst = ["challenger_grandmaster", "master_diamond", "diamond_emerald", "emerald_platinum", "gold", "silver"]
time_lst = ["_early_result.csv", "_middle_result.csv", "_final_result.csv"]
lst = [tier + time for tier in tier_lst for time in time_lst]

combined_data = pd.DataFrame()

for file_name in lst:
    path = "time_duration_results_csv/" + file_name
    data = pd.read_csv(path, index_col=0)

    if combined_data.empty:
        combined_data = data
    else:
        combined_data = combined_data.merge(data, left_index=True, right_index=True, how='outer', suffixes=('', '_' + file_name))

combined_data = combined_data.fillna(0)

combined_data.to_csv('total_time_duration_factors.csv')
