import json
import pandas as pd

# get the square devation
def get_devation(array):
	# get mean value of the array
	df = pd.DataFrame(array)
	mean_value = df.mean()[0]
	# print("Average:", mean_value)
	squared_deviations = (df - mean_value) ** 2
	# print("Square devation: ", squared_deviations)
	sum_square_devation = squared_deviations.values.sum()
	# print("Sum of the square devations", sum_square_devation)
	return sum_square_devation

def get_sum_relations(k, history, avg_val):
	result = 0
	step = 1
	for i in range(0, len(history) - k):
		step = (history[i] - avg_val) * (history[i + k] - avg_val)
		result += step  
	return result
# get the correlation
def get_correlation(history):
	avg_val = df = pd.DataFrame(history)
	mean_value = df.mean()[0]
	square_devation = get_devation(history)
	indexes = []
	relations = []
	for k in range(30, 100, 5):
		indexes.append(k)
		tmp = get_sum_relations(k, history, mean_value)
		relation = tmp / square_devation
		relations.append(relation)
	print(indexes)
	print(relations)
	return 0



if __name__ == "__main__":
	# load the history
	path = "history.json"
	with open(path, "r") as file:
		history = json.load(file)
	get_correlation(history)
