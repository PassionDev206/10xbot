import json

# load the history data
def load_history_from_path(pat):
	with open(path, "r") as file:
		history = json.load(file)
	return history

def calculate_total_profit(history):
	length = len(history)
	total_profit = 0
	profit = 0
	loss = 0
	tmp = 0
	lens = []
	for i in range in length:
		if history[i] < 10:
			tmp += 1
			if tmp > 5 : 
				loss += 1
		else:
			if tmp > 5:
				profit = 10 - (loss + 1)
				total_profit += profit
				lens.append(tmp)
			tmp = 0
	print(lens)
	print("Total profit: ", total_profit)
	return 0

if __name__ == "__main__":
	# load the history data
	path = "history.json"
	history = load_history_from_path(path)
	calculate_total_profit(history)
	