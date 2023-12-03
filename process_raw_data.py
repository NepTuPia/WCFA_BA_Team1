import os
import champ_tier_analysis
import factor_list
import json_functions

relative_factors = factor_list.relative
relative_onehot_factors = factor_list.relative_onehot
team_factors = factor_list.team_factors
team_first_factors = factor_list.team_first_factors
target = factor_list.target
champion_name_code_dict = {'266': 'Aatrox', '103': 'Ahri', '84': 'Akali', '166': 'Akshan', '12': 'Alistar', '32': 'Amumu', '34': 'Anivia', '1': 'Annie', '523': 'Aphelios', '22': 'Ashe', '136': 'AurelionSol', '268': 'Azir', '432': 'Bard', '200': 'Belveth', '53': 'Blitzcrank', '63': 'Brand', '201': 'Braum', '233': 'Briar', '51': 'Caitlyn', '164': 'Camille', '69': 'Cassiopeia', '31': 'Chogath', '42': 'Corki', '122': 'Darius', '131': 'Diana', '119': 'Draven', '36': 'DrMundo', '245': 'Ekko', '60': 'Elise', '28': 'Evelynn', '81': 'Ezreal', '9': 'Fiddlesticks', '114': 'Fiora', '105': 'Fizz', '3': 'Galio', '41': 'Gangplank', '86': 'Garen', '150': 'Gnar', '79': 'Gragas', '104': 'Graves', '887': 'Gwen', '120': 'Hecarim', '74': 'Heimerdinger', '420': 'Illaoi', '39': 'Irelia', '427': 'Ivern', '40': 'Janna', '59': 'JarvanIV', '24': 'Jax', '126': 'Jayce', '202': 'Jhin', '222': 'Jinx', '145': 'Kaisa', '429': 'Kalista', '43': 'Karma', '30': 'Karthus', '38': 'Kassadin', '55': 'Katarina', '10': 'Kayle', '141': 'Kayn', '85': 'Kennen', '121': 'Khazix', '203': 'Kindred', '240': 'Kled', '96': 'KogMaw', '897': 'KSante', '7': 'Leblanc', '64': 'LeeSin', '89': 'Leona', '876': 'Lillia', '127': 'Lissandra', '236': 'Lucian', '117': 'Lulu', '99': 'Lux', '54': 'Malphite', '90': 'Malzahar', '57': 'Maokai', '11': 'MasterYi', '902': 'Milio', '21': 'MissFortune', '62': 'MonkeyKing', '82': 'Mordekaiser', '25': 'Morgana', '950': 'Naafiri', '267': 'Nami', '75': 'Nasus', '111': 'Nautilus', '518': 'Neeko', '76': 'Nidalee', '895': 'Nilah', '56': 'Nocturne', '20': 'Nunu', '2': 'Olaf', '61': 'Orianna', '516': 'Ornn', '80': 'Pantheon', '78': 'Poppy', '555': 'Pyke', '246': 'Qiyana', '133': 'Quinn', '497': 'Rakan', '33': 'Rammus', '421': 'RekSai', '526': 'Rell', '888': 'Renata', '58': 'Renekton', '107': 'Rengar', '92': 'Riven', '68': 'Rumble', '13': 'Ryze', '360': 'Samira', '113': 'Sejuani', '235': 'Senna', '147': 'Seraphine', '875': 'Sett', '35': 'Shaco', '98': 'Shen', '102': 'Shyvana', '27': 'Singed', '14': 'Sion', '15': 'Sivir', '72': 'Skarner', '37': 'Sona', '16': 'Soraka', '50': 'Swain', '517': 'Sylas', '134': 'Syndra', '223': 'TahmKench', '163': 'Taliyah', '91': 'Talon', '44': 'Taric', '17': 'Teemo', '412': 'Thresh', '18': 'Tristana', '48': 'Trundle', '23': 'Tryndamere', '4': 'TwistedFate', '29': 'Twitch', '77': 'Udyr', '6': 'Urgot', '110': 'Varus', '67': 'Vayne', '45': 'Veigar', '161': 'Velkoz', '711': 'Vex', '254': 'Vi', '234': 'Viego', '112': 'Viktor', '8': 'Vladimir', '106': 'Volibear', '19': 'Warwick', '498': 'Xayah', '101': 'Xerath', '5': 'XinZhao', '157': 'Yasuo', '777': 'Yone', '83': 'Yorick', '350': 'Yuumi', '154': 'Zac', '238': 'Zed', '221': 'Zeri', '115': 'Ziggs', '26': 'Zilean', '142': 'Zoe', '143': 'Zyra'}

directory_path = 'silver_data/'
save_directory_path = 'processed_data/silver_data/'
file_list = os.listdir(directory_path)

for file in file_list:
    try:
        match_data = json_functions.open_json(directory_path + file)
        blue_side = [file]
        red_side = [file]
        blue_data_dict = {
            'TOP' : { },
            'JUNGLE' : { },
            'MIDDLE' : { },
            'BOTTOM' : { },
            'UTILITY' : { },
            'COMMON' : { },
        }
        red_data_dict = {
            'TOP' : { },
            'JUNGLE' : { },
            'MIDDLE' : { },
            'BOTTOM' : { },
            'UTILITY' : { },
            'COMMON': { },
        }
        blue_champions = []
        red_champions = []
        # each lane factors process
        for player_data in match_data["info"]["participants"]:
            if player_data["teamId"] == 100:
                lane = player_data["teamPosition"]
                for relative_factor in relative_factors:
                    blue_data_dict[lane][lane + '_' + relative_factor + '_gap'] = int(player_data[relative_factor])
                    red_data_dict[lane][lane + '_' + relative_factor + '_gap'] = -int(player_data[relative_factor])

                for relative_onehot_factor in relative_onehot_factors:
                    blue_data_dict[lane][lane + '_' + relative_onehot_factor + '_gap'] = 1 if player_data[relative_onehot_factor] else 0
                    red_data_dict[lane][lane + '_' + relative_onehot_factor + '_gap'] = -(1 if player_data[relative_onehot_factor] else 0)
                blue_champions.append(player_data["championName"])
            else:
                lane = player_data["teamPosition"]
                for relative_factor in relative_factors:
                    red_data_dict[lane][lane + '_' + relative_factor + '_gap'] += int(player_data[relative_factor])
                    blue_data_dict[lane][lane + '_' + relative_factor + '_gap'] -= int(player_data[relative_factor])

                for relative_onehot_factor in relative_onehot_factors:
                    blue_data_dict[lane][lane + '_' + relative_onehot_factor + '_gap'] += 1 if player_data[relative_onehot_factor] else 0
                    red_data_dict[lane][lane + '_' + relative_onehot_factor + '_gap'] -= (1 if player_data[relative_onehot_factor] else 0)
                red_champions.append(player_data["championName"])

        # team total factors process
        for relative_factor in relative_factors:
            blue_total_data = 0
            red_total_data = 0
            for lane in blue_data_dict:
                if lane == 'COMMON':
                    continue
                blue_total_data += blue_data_dict[lane][lane + '_' + relative_factor + '_gap']
                red_total_data += red_data_dict[lane][lane + '_' + relative_factor + '_gap']

            blue_data_dict['COMMON']['total_' + relative_factor + '_gap'] = blue_total_data
            red_data_dict['COMMON']['total_' + relative_factor + '_gap'] = red_total_data

        for team_factor in team_factors:
            blue_data_dict['COMMON']["total_" + team_factor] = match_data["info"]["participants"][0][team_factor]
            red_data_dict['COMMON']["total_" + team_factor] = match_data["info"]["participants"][5][team_factor]

        for team_first_factor in team_first_factors:
            team_data = match_data["info"]["teams"][0]
            blue_data_dict['COMMON']["total_" + team_first_factor +"_first"] = 1 if team_data['objectives'][team_first_factor]['first'] else 0
            team_data = match_data["info"]["teams"][1]
            red_data_dict['COMMON']["total_" + team_first_factor + "_first"] = 1 if team_data['objectives'][team_first_factor]['first'] else 0

        blue_data_dict['COMMON']['champions'] = blue_champions
        red_data_dict['COMMON']['champions'] = red_champions

        tier = "silver"
        blue_avg_champ_tier = champ_tier_analysis.get_avg_champ_tier(blue_champions, tier)
        red_avg_champ_tier = champ_tier_analysis.get_avg_champ_tier(red_champions, tier)
        blue_data_dict['COMMON']['avg_champ_tier_gap'] = '%.1f' % (blue_avg_champ_tier - red_avg_champ_tier)
        red_data_dict['COMMON']['avg_champ_tier_gap'] = '%.1f' % (red_avg_champ_tier - blue_avg_champ_tier)

        blue_data_dict['COMMON']['game_duration'] = match_data['info']['gameDuration']
        red_data_dict['COMMON']['game_duration'] = match_data['info']['gameDuration']

        team_data = match_data["info"]["teams"][0]
        blue_data_dict['COMMON']['win'] = 1 if team_data[target] else 0

        team_data = match_data["info"]["teams"][1]
        red_data_dict['COMMON']['win'] = 1 if team_data[target] else 0

        json_functions.save_dict("processed_data/silver_data/" + file.split('.')[0] + "_blue.json", blue_data_dict)
        json_functions.save_dict("processed_data/silver_data/" + file.split('.')[0] + "_red.json", red_data_dict)
    except:
        print("Something wrong data in " + file)
        continue
