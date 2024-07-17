import hmac
import hashlib
import json

# get the crash value from the hash value and salt
def get_crash_from_hash(hash, salt):
	# hash the hash value using the hmac hash function
	hash = hmac.new(salt.encode(), bytes.fromhex(hash), hashlib.sha256).hexdigest()
	n_bits = 52
	r = int(hash[:n_bits // 4], 16)
	X = r / (2 ** n_bits)
	X = float(f'{X:.9f}')
	X = 99 / (1 - X)
	result = int(X)
	return max(1, result / 100)

# get the previous hash value
def get_previous_hash(hash):
	return hashlib.sha256(hash.encode()).hexdigest()

# get the crash history 
def get_crash_history(hash, salt, index):
	test_data = []
	train_data = []
	end_point = index - 1530000
	cnt = 0
	while index > end_point:
		cnt += 1
		crash_value = get_crash_from_hash(hash, salt)
		if cnt < 30000:
			test_data.append(crash_value)	
		else:
			train_data.append(crash_value)
		index -= 1
		hash = get_previous_hash(hash)

	test_data.reverse()
	train_data.reverse()
	
	train_path = "train_data.json"
	with open(train_path, "w") as file:
		json.dump(train_data, file, indent=2)
	
	test_path = "test_data.json"
	with open(test_path, "w") as file:
		json.dump(test_data, file, indent=2)
	print('Build history data')
	return 0

if __name__ == "__main__":
	# define the value of hash, salt, and index
	hash = "2c04a07be39e28d8e3784360f9f96d2fa388054bd18aa0306963f0098083cdf3"
	salt = "0000000000000000000301e2801a9a9598bfb114e574a91a887f2132f33047e6"
	gameId = 7220169

	get_crash_history(hash, salt, gameId)


