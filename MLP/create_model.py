import numpy as np
import json
import tensorflow as tf
from keras.src.models import Sequential
from keras.src.layers import Dense
from sklearn.model_selection import train_test_split

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

# create the input & output dataset for training
def create_dataset(data, sequence_length):
	x  = []
	y = []
	for i in range(len(data) - sequence_length):
		x.append(data[i:i + sequence_length])
		y.append(data[i + sequence_length])
    
	x = np.array(x)
	y = np.array(y)
	return x, y

# evaluate the accuracy
def get_evaluation(actual, prediction, threshold):
	greater_num = 0
	correct_num = 0
	for i in range(len(actual)):
		if prediction[i] == 1:
			greater_num += 1
			if actual[i] == 1:
				correct_num += 1
	print(f"Correct number: {correct_num}")
	print(f"Total prediction number: {greater_num}")
	accuracy = correct_num / greater_num * 100

	profit = (threshold - 1) * correct_num - (greater_num - correct_num)
	print(f"Profit from {threshold} is {profit}")
	return accuracy

# create the model
def initiate_model(trainX, trainY, testX, testY, epoch, batch_size, loss_function='binary_crossentropy', optimizer='adam', threshold=1):
	# initiate the model
	model = Sequential([
    Dense(100, input_shape=(sequence_len,), activation='relu'),
    Dense(50, activation="relu"),
		Dense(1, activation='sigmoid')  # Output layer with sigmoid activation for binary prediction
	])
	# compile the model
	model.compile(optimizer=optimizer, loss=loss_function, metrics=['accuracy'])
	# fit the model
	model.fit(trainX, trainY, epochs=epoch, batch_size=batch_size, validation_data=(testX, testY))

	# evaluate the model
	y_pred = model.predict(X_train)
	y_pred = np.array(y_pred > 0.5).astype(int).flatten()

	# Calculate accuracy
	accuracy = get_evaluation(testY, y_pred, threshold)
	print("Accuracy: ", accuracy)
	return model


if __name__ == "__main__":
	# load the crash data
	data_path = "history100k.json"
	# input sequence length
	sequence_len = 256
	# input the threshold data 
	threshold = input("Input the threshold value:")
	threshold = float(threshold)
	# load the crash history data
	training_data = get_data_from_path(data_path)
	# convert the crash history data to binary data
	training_data = convert_binary_data(training_data, threshold)
	# create input and output dataset
	inputX, outputY = create_dataset(training_data, sequence_len)
	# split the training data to train and test set
	X_train, X_test, y_train, y_test = train_test_split(inputX, outputY, test_size=0.2, random_state=42)
	# create the prediction model
	model = initiate_model(X_train, y_train, X_test, y_test, epoch=64, batch_size=32, loss_function='binary_crossentropy', optimizer='adam', threshold = threshold)

