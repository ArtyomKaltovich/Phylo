import requests

DATA_URL = r"https://www.jasondavies.com/tree-of-life/life.txt"


def save_data_to_file(file_name):
    data = requests.get(DATA_URL)
    data = data.text
    with open(file_name, "w") as file:
        file.write(data)
