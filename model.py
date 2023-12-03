import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.stats.outliers_influence import variance_inflation_factor
import csv_functions as csv

def save_list_to_text_file(lst, file_path):
    with open(file_path, 'w') as file:
        for item in lst:
            file.write(str(item) + '\n')
def calculate_vif(data, threshold=5.0):
    X = data.drop('win', axis=1)

    vif_data = pd.DataFrame()
    vif_data["Variable"] = X.columns
    vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

    high_vif_variables = vif_data[vif_data['VIF'] > threshold]['Variable']
    return high_vif_variables
def remove_high_vif_features(data, threshold=5.0):
    high_vif_variables = calculate_vif(data, threshold)
    data_filtered = data.drop(high_vif_variables, axis=1)

    return data_filtered

def print_correlation(data):
    threshold = 0.3
    correlation_matrix = data.corr()

    sorted_correlation = correlation_matrix.unstack().sort_values(ascending=False)

    sorted_correlation = sorted_correlation[~(sorted_correlation.index.get_level_values(0) == sorted_correlation.index.get_level_values(1))]

    selected_correlation = sorted_correlation[sorted_correlation >= threshold]

    print(selected_correlation)

def model(data):
    X = data.drop('win', axis=1)
    y = data['win']
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    models = {
        'Logistic Regression': LogisticRegression(),
    }

    pipeline = Pipeline([
        ('scaler', None),
        ('classifier', None)
    ])

    param_grid = {
        'scaler' : [StandardScaler(), MinMaxScaler()],
        'classifier': [LogisticRegression()],
        'classifier__C': [0.1, 1, 10],  # 로지스틱 회귀의 C 값
        'classifier__penalty' : ["l1", "l2"],
        'classifier__solver' : ['liblinear', 'saga']
    }

    grid_search = GridSearchCV(pipeline, param_grid=param_grid, cv=5, scoring='accuracy')

    grid_search.fit(X_train, y_train)

    best_model = grid_search.best_estimator_.named_steps['classifier']
    print(f'Best Model: {best_model}')
    result_txt.append(['Best Model', best_model])

    best_scaler = grid_search.best_estimator_.named_steps['scaler']
    print(f'Best Scaler: {best_scaler}')
    result_txt.append(['Best Scaler', best_scaler])

    y_pred = grid_search.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy}')
    result_txt.append(['Accuracy', accuracy])
    coefficients = best_model.coef_

    cnt = 0
    feature_coef_list = []
    for feature, coef in zip(X.columns, coefficients[0]):
        print(f"{feature}: {coef}")
        result_txt.append([feature, coef])
        feature_coef_list.append([feature, coef])
        cnt += 1
    print(cnt)
    return feature_coef_list


tier_lst = ["challenger_grandmaster","master_diamond", "diamond_emerald", "emerald_platinum", "gold", "silver"]
time_lst = ["_early.csv", "_middle.csv", "_final.csv"]
lst = []
for tier in tier_lst:
    for time in time_lst:
        lst.append(tier + time)
for file_name in lst:
    path = "processed_time_duration_data/" + file_name
    data = pd.read_csv(path)
    data = data.dropna(axis=1)
    data = data.drop("game_duration_label", axis = 1)
    feature_name = data.columns

    index = 0
    for i in feature_name:
        if i.split('_')[0] in ["TOP", "JUNGLE", "MIDDLE", "BOTTOM", "UTILITY"]:
            index += 1

    total_index = [feature_name[index], feature_name[len(feature_name)-1]]
    total_data = data.loc[:,total_index[0]:total_index[1]]
    total_data_low_vif = remove_high_vif_features(total_data, 10)
    result_txt = []
    result_txt.append(['Data', file_name.split('.csv')[0]])
    # calculate_each_accuracy(total_data)
    feature_coef_list = model(total_data_low_vif)
    # save_list_to_text_file(feature_coef_list, "time_duration_results/"+ file_name.split(".")[0] + "_result.txt")
    feature_coef_list = sorted(feature_coef_list, key=lambda x: x[1], reverse=True)

    save_folder = "time_duration_results_csv/"
    csv.save_model_result_to_csv(result_txt, save_folder+file_name.split('.')[0] + "_result.csv")

#deprecated
    # feature_coef_list = sorted(feature_coef_list, key=lambda x: x[1], reverse=True)
    #
    # top5_positive_factors = [x[0] for x in feature_coef_list[:5]]
    # top5_negative_factors = [x[0] for x in feature_coef_list[-5:]]
    # print(top5_positive_factors)
    # print(top5_negative_factors)
    # top5_data = {}
    # for factor in top5_positive_factors + top5_negative_factors:
    #     top5_data[factor] = data[factor]
    #
    # top5_data['TargetColumn'] = data['avg_champ_tier_gap']
    #
    # df = pd.DataFrame(top5_data)
    #
    # correlation_matrix = df.corr()
    # print(correlation_matrix)
    # correlations_with_target = correlation_matrix['TargetColumn'].drop('TargetColumn')
    #
    # correlations_with_target.plot(kind='bar', color='blue')
    # plt.xticks(rotation = 45)
    #
    # plt.title('Correlation between team_avg_champ_tier and most dominant factors, Diamond and master')
    # plt.xlabel('domainant factors')
    # plt.ylabel('correlation')
    #
    # plt.show()