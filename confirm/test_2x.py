import numpy as np

def get_normal_profit(data):
	# bet_cnt = len(data)
	bet_cnt = 3000
	total_profit = 0
	loss_cnt = 0
	loss_array = []
	loss_amount = 0
	for i in range(bet_cnt):
		if data[i] >= 2:
			total_profit += 1
			loss_array.append(loss_cnt)
			loss_cnt = 0
		else:
			loss_cnt += 1
				
	total_profit -= loss_amount
	print("Total loss:", loss_amount)	
	print("Total profit", total_profit)
	loss_array = np.array(loss_array)
	np.savetxt("daily_loss.txt", loss_array, fmt="%.0f")
	print("Max loss count: ", loss_array.max())
	return 0

def get_profit_from_threshold(data, threshold):
	daily_bet_cnt = 3000
	day_num = 300
	total_profit = 0
	for k in range(day_num):
		daily_profit = 0
		loss_cnt = 0
		# loss_array = []
		loss_amount = 0
		for i in range(daily_bet_cnt):
			if data[k * daily_bet_cnt + i] >= 2:
				daily_profit += 1
				# loss_array.append(loss_cnt)
				loss_cnt = 0
			else:
				loss_cnt += 1
				if loss_cnt == threshold:
					loss_cnt = 0
					loss_amount += 2 ** threshold - 1	

		daily_profit -= loss_amount
		total_profit += daily_profit
		print(f"{k} Day's result!!!!!!!")
		print("Total loss:", loss_amount)	
		print("Daily profit", daily_profit)
	print(f"Total profit of {day_num} days: ", total_profit)
	return 0

if __name__ == "__main__":
	# load the test data
	path = "train_data.txt"
	data = np.loadtxt(path).ravel()

	method = input("Input the test method:")
	method = int(method)

	if(method == 1):
		get_normal_profit(data)
	elif(method == 2):
		threshold = input("Input the threshold value: ")
		threshold = int(threshold)
		get_profit_from_threshold(data, threshold)
