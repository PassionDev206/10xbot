import numpy as np
import json

# load the data from the json file
def get_data_from_path(path):
	with open(path, "r") as file:
		data = json.load(file)
	return data

# convert the data to binary data
def convert_binary_data(raw_data, threshold):
	binary_data = []
	for i in range(len(raw_data)):
		if raw_data[i] < threshold:
			binary_data.append(0)
		else:
			binary_data.append(1)
	return binary_data


if __name__ == "__main__":
	# load the crash data
	data_path = "history100k.json"
	# input the threshold data 
	threshold = input("Input the threshold value:")
	threshold = float(threshold)
	# load the crash history data
	training_data = get_data_from_path(data_path)
	# convert the crash history data to binary data
	training_data = convert_binary_data(training_data, threshold)
	
	