import json

# load the history data
def load_history_from_path(pat):
	with open(path, "r") as file:
		history = json.load(file)
	return history

def calculate_total_profit(history):
	total_profit = 0
	profit = 0
	loss = 0
	tmp = 0
	lens = []
	profits = []
	loss_cnt = 0
	profit_cnt = 0
	max_loss = 0
	for i in range(1000000):
		if history[i] < 10:
			tmp += 1
			if tmp > 6: 
				loss += 1
		else:
			if tmp > 6:
				profit = 10 - loss
				if profit < 0:
					loss_cnt += 1
					if profit < max_loss:
						max_loss = profit
				else:
					profit_cnt += 1
				total_profit += profit
				lens.append(tmp)
				profits.append(profit)
			tmp = 0
			loss = 0
	print(profits)
	with open("result_10x/length.json", "w") as file:
		json.dump(lens, file, indent=2)
	with open("result_10x/profits.json", "w") as file:
		json.dump(profits, file, indent=2)
	total_cnt = len(lens)
	result = {
		"Total betting number: ": f"{total_cnt}",
		"Profit number: ": f"{profit_cnt}",
		"Loss number: ": f"{loss_cnt}",
		"Max loss: ": f"{max_loss}",
		"Total profit:": f"{total_profit}"
	}

	with open("result_10x/result.json", "w") as file:
		json.dump(result, file, indent=2)
	print("Total profit: ", total_profit)
	return 0

if __name__ == "__main__":
	# load the history data
	path = "history.json"
	history = load_history_from_path(path)
	calculate_total_profit(history)
