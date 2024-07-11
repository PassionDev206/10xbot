import numpy as np
import pandas as pd
import json
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# create the dataset (input and output) for training
def create_dataset(data, sequence_length):
	x  = []
	y = []
	for i in range(len(data) - sequence_length):
		x.append(data[i:i + sequence_length])
		y.append(data[i + sequence_length])
    
	x = np.array(x)
	y = np.array(y)
	return x, y

# load the data from json file 
def load_data_from_path(path):
	with open(path, "r") as file:
		data = json.load(file)
	return data

# convert raw data to the binary data
def convert_to_binary(data, thresold):
	binary_data = []
	for i in range(len(data)):
		binary_data.append(int(data[i] >= thresold))
	return binary_data

# evaluate the model with test result and actual values
def evaluate_model(actual, predictions, threshold):
	correct_num = 0
	total_num = len(actual)
	for i in range(total_num):
		if predictions[i] > 0:
			if actual[i] > 0:
				correct_num += 1
	accuracy = correct_num / total_num * 100
	print(f"The accuracy in {threshold} is {accuracy:.2}%")
	profit = correct_num * (threshold - 1) - (total_num - correct_num)
	print(f"The profit from {threshold} is {profit:.2f}")

if __name__ == "__main__":
	data = load_data_from_path("history100k.json")
	thresold = input("Input the threshold: ")
	binary_data = convert_to_binary(data, float(thresold))
	input_data, output_data = create_dataset(binary_data, 10)
	X_train, X_test, y_train, y_test = train_test_split(input_data, output_data, test_size=0.2)

	# Train the SVM model
	svm_model = SVC(kernel='linear')
	svm_model.fit(X_train, y_train)

	# Make predictions
	y_pred = svm_model.predict(X_test)
	with open("result.json", "w") as file:
		json.dump(y_pred.tolist(), file, indent=2)
	
	with open("actual.json", "w") as file:
		json.dump(y_test.tolist(), file, indent=2)
	# Evaluate the model with test result
	evaluate_model(y_test, y_pred, float(thresold))
	