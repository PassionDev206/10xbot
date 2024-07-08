import numpy as np
import json
import tensorflow as tf
from keras.src.models import Sequential
from keras.src.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

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
		X.append(data[i:i + sequence_length])
		y.append(data[i + sequence_length])
    
	X = np.array(X)
	y = np.array(y)
	return X, y

# create the model
def initiate_model(trainX, trainY, testX, testY, epoch, batch_size, loss_function='binary_crossentropy', optimizer='adam'):
	# initiate the model
	model = Sequential([
    Dense(100, input_shape=(sequence_len,), activation='relu'),
    Dense(50, activation="relu"),
		Dense(50, activation="relu"),
		Dense(1, activation='sigmoid')  # Output layer with sigmoid activation for binary prediction
	])
	# compile the model
	model.compile(optimizer=optimizer, loss=loss_function, metrics=['accuracy'])
	# fit the model
	model.fit(trainX, trainY, epochs=epoch, batch_size=batch_size, validation_data=(testX, testY))

	# evaluate the model
	y_pred = model.predict(X_test)
	y_pred = int(y_pred > 0.5) 

	# Calculate accuracy
	accuracy = accuracy_score(y_test, y_pred)
	print(f'Test Accuracy: {accuracy * 100:.2f}%')
	return model


if __name__ == "__main__":
	# load the crash data
	data_path = "history100k.json"
	# input sequence length
	sequence_len = 20
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
	model = initiate_model(X_train, X_test, y_train, y_test, 'binary_crossentropy', 'adam')

# # Example sequence to predict the next value
# test_sequence = data[-sequence_len:]

# # Predict the next value
# next_value = model.predict(np.reshape(test_sequence, (1, sequence_len)))
# next_value = int(next_value > 0.5)
# print(f'Predicted next value: {next_value[0][0]}')
