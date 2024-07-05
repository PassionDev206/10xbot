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
	max_len = 0
	large_lens = []
	for i in range(1000000):
		if history[i] >= 2:
			lens.append(tmp)
			if tmp > 9:
				large_lens.append(tmp)
				if tmp > max_len:
					max_len = tmp
			tmp = 0
		else:
			tmp += 1
	
	with open("result_2x/lens.json", "w") as file:
		json.dump(lens, file, indent=2)
	
	large_cnt = len(large_lens)
	total_profit = len(lens)
	result = {
		"Large number: ": f"{large_cnt}",
		"Max count: ": f"{max_len}",
		"Total profit: ": f"{total_profit}"
	}
	with open("result_2x/result.json", "w") as file:
		json.dump(result, file, indent=2)
	return 0

if __name__ == "__main__":
	# load the history data
	path = "history.json"
	history = load_history_from_path(path)
	get_max_length_without_2x(history)
	