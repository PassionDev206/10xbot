import json
import numpy as np
# load the history data
def load_history_from_path(pat):
	with open(path, "r") as file:
		history = json.load(file)
	return history

# calculate the risk of the 2x strategy
def get_max_length_without_2x(history):
	lens = []
	tmp = 0
	for i in range(1000000):
		if history[i] >= 2:
			lens.append(tmp)
			tmp = 0
		else:
			tmp += 1

	print(lens) 
	with open("lens.json", "w") as file:
		json.dump(lens, file, indent=2)
	print("Profits: ", len(lens))
	lens = np.array(lens)
	print("Max: ", np.max(lens))
	return 0

if __name__ == "__main__":
	# load the history data
	path = "history.json"
	history = load_history_from_path(path)
	get_max_length_without_2x(history)
	