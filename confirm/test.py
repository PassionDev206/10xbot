import json

# test to get the profit in specific crash value
def test_getting_profit():
	with open("history.json") as file:
		history = json.load(file)
	profit_cnt = 0
	loss_cnt = 0
	profit_range = input("Profit range:")
	profit_range = float(profit_range)
	temp = 0
	total_profit = 0
	high_crash = 1
	high_bet_flag = False
	cnt = 0
	daily_profit = []
	temp_profit = 0
	for i in range(1000000):
		cnt += 1
		if history[i] < (1 + profit_range):
			if high_bet_flag == True:
				total_profit -= high_crash
			else:
				total_profit -= 1
			loss_cnt += 1
			high_bet_flag = True
		else:
			profit_cnt += 1
			if high_bet_flag == True:
				temp += 1
				total_profit += high_crash * profit_range
				if temp == 1:
					high_bet_flag = False
					temp = 0
			else:
				total_profit += profit_range
		if cnt % 3000 == 0:
			daily_profit.append(total_profit - temp_profit)
			temp_profit = total_profit

	with open("daily_profit1.json", "w") as file:
		json.dump(daily_profit, file, indent=2)
	print("Loss count: ", loss_cnt)
	print("Profit count:", profit_cnt)
	# total_profit = profit_range * profit_cnt - loss_cnt
	print("Total profit: ", total_profit)

# test the risk management in 2x strategy
def test_risk_2x():
	path = "history.json"
	with open(path, "r") as file:
		data = json.load(file)
	temp = 0
	lens = []
	for i in range(len(data)):
		if data[i] < 2:
			temp += 1
		else:
			lens.append(temp)
			temp = 0
	print(lens)

if __name__ == "__main__":
	test_method = input("Input the test method:")
	test_method = int(test_method)
	if test_method == 0:
		test_getting_profit()
	elif test_method == 1:
		test_risk_2x()