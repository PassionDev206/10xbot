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
	profits = []
	for i in range(1000000):
		if history[i] < 10:
			tmp += 1
			if tmp > 9: 
				loss += 1
		else:
			if tmp > 9:
				profit = 10 - loss
				total_profit += profit
				lens.append(tmp)
				profits.append(profit)
			tmp = 0
			loss = 0
	print(lens)
	print(profits)
	print("Total profit: ", total_profit)
	return 0

if __name__ == "__main__":
	# load the history data
	path = "history.json"
	history = load_history_from_path(path)
	calculate_total_profit(history)
	