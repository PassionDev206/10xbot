import json

if __name__ == "__main__":
	with open("lens.json", "r") as file:
		history = json.load(file)

	indexes = []
	max = []
	for i in range(len(history)):
		if history[i] >= 10:
			indexes.append(i)
			max.append(history[i])

	print(max)
	print(indexes)