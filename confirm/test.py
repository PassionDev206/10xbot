import json
import numpy as np

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

# get the array of the length how many times appear greater than 2x or less than 2x
def get_length_list(data):
	lens = []
	temp = 0
	for i in range(len(data)):
		if data[i] < 2:
			temp += 1
		else:
			lens.append(temp)
			temp = 0
	return lens

# test the risk management in 2x strategy
def test_risk_2x():
	path = "history.json"
	with open(path, "r") as file:
		data = json.load(file)
	lens = get_length_list(data)

	array = np.array(lens)
	max_len = np.max(array)
	total_len = len(lens)
	print(max_len)
	result_f = []
	result_p = []
	for i in range(max_len):
		frequiecy = 0
		for j in range(total_len):
			if lens[j] == i:
				frequiecy += 1
		result_f.append(frequiecy)
		result_p.append(frequiecy / total_len * 100)
	with open("frequency_2x.json", "w") as file:
		json.dump(result_f, file, indent=2)
	with open("percent_2x.json", "w") as file:
		json.dump(result_p, file, indent=2)

# calculate the daily risk
def get_max_length_without_2x(history, drop_range):
	lens = []
	tmp = 0
	max_len = 0
	large_lens = []
	for i in range(3500):
		if history[i] >= 2:
			lens.append(tmp)
			if tmp > drop_range:
				large_lens.append(tmp)
				if tmp > max_len:
					max_len = tmp
			tmp = 0
		else:
			tmp += 1
	
	with open("lens.json", "w") as file:
		json.dump(lens, file, indent=2)
	
	large_cnt = len(large_lens)
	total_profit = len(lens)
	result = {
		"Large number: ": f"{large_cnt}",
		"Max count: ": f"{max_len}",
		"Total profit: ": f"{total_profit}"
	}
	with open("result.json", "w") as file:
		json.dump(result, file, indent=2)
	return 0

# get the daily profit
def get_daily_profit(history, drop_range):
	with open("data.json", "w") as file:
		json.dump(history, file, indent=2)
	total_bet = 0
	total_profit = 0
	bet_amount = 1
	profit_amount = 0
	profit_cnt = 0
	loss_cnt = 0
	for i in range(3500):
		total_bet += bet_amount
		if history[i] >= 2:
			profit_amount += 2 * bet_amount
			bet_amount = 1
			profit_cnt += 1
			loss_cnt = 0
		else:
			bet_amount = bet_amount * 2
			loss_cnt += 1

	total_profit = profit_amount - total_bet

	print("Bet count: ", profit_cnt)
	print("Total profit: ", total_profit)

	return 0

# test risk management in 2x strategy to minimize the loss
def test_risk_management():
	path = "history.json"
	with open(path, "r") as file:
		data = json.load(file)
	
	day = input("Index of the day: ")
	day = int(day) - 1

	daily_history = []
	for i in range(3500):
		daily_history.append(data[day * 3500 + i])
	
	get_max_length_without_2x(daily_history, 7)
	get_daily_profit(daily_history, 7)

if __name__ == "__main__":
	test_method = input("Input the test method:")
	test_method = int(test_method)
	if test_method == 0:
		test_getting_profit()
	elif test_method == 1:
		test_risk_2x()
	elif test_method == 2:
		test_risk_management()
	