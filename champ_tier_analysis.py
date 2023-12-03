import pandas as pd
import champ_tier_final
import matplotlib.pyplot as plt
file_path = 'processed_raw_data/'
file = 'challenger_gm_data.csv'

def get_avg_champ_tier(champ_list, tier):
    tier_list = None
    if tier == 'challenger_grandmaster': tier_list = champ_tier_final.gm
    elif tier == "master_diamond": tier_list = champ_tier_final.master
    elif tier == "diamond_emerald": tier_list = champ_tier_final.dia
    elif tier == "platinum": tier_list = champ_tier_final.platinum
    elif tier == "gold": tier_list = champ_tier_final.gold
    elif tier == "silver": tier_list = champ_tier_final.silver

    top_tier_dict = {}
    for data in tier_list[0]:
        top_tier_dict[data[1]] = [data[0]]

    jungle_tier_data = {}
    for data in tier_list[1]:
        jungle_tier_data[data[1]] = [data[0]]

    mid_tier_data = {}
    for data in tier_list[2]:
        mid_tier_data[data[1]] = [data[0]]

    bot_tier_data = {}
    for data in tier_list[3]:
        bot_tier_data[data[1]] = [data[0]]

    util_tier_data = {}
    for data in tier_list[4]:
        util_tier_data[data[1]] = [data[0]]

    tier_weight = {
        1: 5,
        2: 4,
        3: 3,
        4: 2,
        5: 1,
        None: 0
    }
    no_tier_champ_error_count = 0
    no_tier_champ_error_count_count = 0

    champ_list_kr = []
    for champ in champ_list:
        champ_list_kr.append(champ_tier_final.champion_dict_reversed[champ])

    champ_tier_score = 0
    valid_champion_number = 5

    swap_tier_list1 = None
    swap_index1 = None
    swap_tier_list2 = None
    swap_index2 = None
    try:
        champ_tier_score += tier_weight[top_tier_dict[champ_list_kr[0]][0]]
    except Exception as e:
        no_tier_champ_error_count += 1
        if swap_tier_list1 == None:
            swap_tier_list1 = top_tier_dict
            swap_index1 = 0
        else:
            swap_tier_list2 = top_tier_dict
            swap_index2 = 0
    try:
        champ_tier_score += tier_weight[jungle_tier_data[champ_list_kr[1]][0]]
    except Exception as e:
        no_tier_champ_error_count += 1
        if swap_tier_list1 == None:
            swap_tier_list1 = jungle_tier_data
            swap_index1 = 1
        else:
            swap_tier_list2 = jungle_tier_data
            swap_index2 = 1
    try:
        champ_tier_score += tier_weight[mid_tier_data[champ_list_kr[2]][0]]
    except Exception as e:
        no_tier_champ_error_count += 1
        if swap_tier_list1 == None:
            swap_tier_list1 = mid_tier_data
            swap_index1 = 2
        else:
            swap_tier_list2 = mid_tier_data
            swap_index2 = 2
    try:
        champ_tier_score += tier_weight[bot_tier_data[champ_list_kr[3]][0]]
    except Exception as e:
        no_tier_champ_error_count += 1
        if swap_tier_list1 == None:
            swap_tier_list1 = bot_tier_data
            swap_index1 = 3
        else:
            swap_tier_list2 = bot_tier_data
            swap_index2 = 3
    try:
        champ_tier_score += tier_weight[util_tier_data[champ_list_kr[4]][0]]
    except Exception as e:
        no_tier_champ_error_count += 1
        if swap_tier_list1 == None:
            swap_tier_list1 = util_tier_data
            swap_index1 = 4
        else:
            swap_tier_list2 = util_tier_data
            swap_index2 = 4

    if no_tier_champ_error_count <= 1:
        valid_champion_number = 5
    elif no_tier_champ_error_count == 2:
        try:
            champ_tier_score += tier_weight[swap_tier_list1[champ_list_kr[swap_index1]][0]]
        except Exception as e:
            no_tier_champ_error_count_count += 1
        try:
            champ_tier_score += tier_weight[swap_tier_list2[champ_list_kr[swap_index2]][0]]
        except Exception as e:
            no_tier_champ_error_count_count += 1
        if no_tier_champ_error_count_count <= 1:
            valid_champion_number = 5

    champ_tier_score /= valid_champion_number
    return champ_tier_score


path = "processed_raw_data/challenger_grandmaster_data.csv"
data = pd.read_csv(path)
data = data.dropna(axis=1)
tier_data = data["avg_champ_tier_gap"]
win_data = data["win"]

result_win_dict = {}
result_lose_dict = {}

for tier, win in zip(tier_data, win_data):
    if win == 1:
            if result_win_dict.get(tier) == None:
                result_win_dict[tier] = 1
            else:
                result_win_dict[tier] += 1
    elif win == 0:
        if result_lose_dict.get(tier) == None:
            result_lose_dict[tier] = 1
        else:
            result_lose_dict[tier] += 1


result_win_keys = sorted(result_win_dict, reverse=True)
result_lose_keys = sorted(result_lose_dict, reverse=True)
result_win_list = []
result_lost_list = []

for key in result_win_keys:
    result_win_list.append(result_win_dict[key])
for key in result_lose_keys:
    result_lost_list.append(result_lose_dict[key])

plt.plot(result_win_keys, result_win_list, label='team_avg_champ_tier & win', color='blue', marker='o', linestyle='-')
plt.plot(result_lose_keys, result_lost_list, label='team_avg_champ_tier & lose', color='red', marker='x', linestyle='--')

plt.title('Master_Diamond tier')
plt.xlabel('team_avg_champ_tier')
plt.ylabel('Win or lose count')

plt.legend()

plt.show()