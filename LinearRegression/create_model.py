import json
import numpy as np

# load the history data from json file
def load_data_from_path(path):
	with open(path, "w") as file:
		data = json.load(file)
	return data

# convert raw history data to binary data
def convert_to_binary(data, threshold):
	binary_data = []
	for i in range(len(data)):
		binary_data.append(data[i] >= threshold)
	return binary_data

if __name__ == "__main__":
	data = load_data_from_path("history100k.json")
	threshold = input("Input the threshold: ")
	binary_data = convert_to_binary(data, threshold)
	

