import csv


def save_to_csv(data, filename):
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
        print(f"Data successfully saved to {filename}.")
    except Exception as e:
        print(f"Error while saving the data: {e}")

def save_model_result_to_csv(data, filename):
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print(f"Data successfully saved to {filename}.")
    except Exception as e:
        print(f"Error while saving the data: {e}")
def append_to_csv(file_path, data):
    # CSV 파일 열기 (없으면 새로 생성)
    with open(file_path, 'a', newline='') as csvfile:
        # CSV writer 객체 생성
        csv_writer = csv.writer(csvfile)

        # 주어진 데이터를 CSV 파일에 추가
        csv_writer.writerow(data)

def read_first_column(file_path):
    # 결과를 저장할 리스트
    first_column_values = []

    # CSV 파일 열기
    with open(file_path, 'r') as csvfile:
        # CSV reader 객체 생성
        csv_reader = csv.reader(csvfile)

        # 각 행의 첫 번째 값 리스트에 추가
        for row in csv_reader:
            first_column_values.append(row[0])
    return first_column_values
def read_second_column(file_path):
    # 결과를 저장할 리스트
    second_column_values = []

    # CSV 파일 열기
    with open(file_path, 'r') as csvfile:
        # CSV reader 객체 생성
        csv_reader = csv.reader(csvfile)

        # 각 행의 첫 번째 값 리스트에 추가
        for row in csv_reader:
            second_column_values.append(row[1])
    return second_column_values