import json

if __name__ == "__main__":
	with open("history.json") as file:
		history = json.load(file)
	profit_cnt = 0
	loss_cnt = 0
	dif = []
	profit_range = input("Profit range:")
	profit_range = float(profit_range)
	temp = 0
	cnt = 0
	total_profit = 0
	daily_profit = []
	temp_profit = 0
	for i in range(1000000):
		cnt += 1
		if history[i] < 1 + profit_range:
			total_profit -= 1
			loss_cnt += 1
			temp += 1
		else:
			profit_cnt += 1
			total_profit += profit_range
			if temp > 0:
				dif.append(temp)
				temp = 0
		if cnt % 3000 == 0:
			daily_profit.append(total_profit - temp_profit)
			temp_profit = total_profit

	with open("difference.json", "w") as file:
		json.dump(dif, file, indent=2)
	with open("daily_profit.json", "w") as file:
		json.dump(daily_profit, file, indent=2)
	print("Loss count: ", loss_cnt)
	print("Profit count:", profit_cnt)
	print("Total profit: ", total_profit)