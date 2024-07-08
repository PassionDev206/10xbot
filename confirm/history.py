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
def get_crash_history(hash, salt, index, len):
	end_point = index - len
	data = []
	while index > end_point:
		crash_value = get_crash_from_hash(hash, salt)
		data.append(crash_value)
		index -= 1
		hash = get_previous_hash(hash)

	data.reverse()
	file = f"history100k.json"
	with open(file, "w") as file:
		file.write(json.dumps(data, indent=2))
	file.close()

	print('Build history data')
	return 0

if __name__ == "__main__":
	# define the value of hash, salt, and index
	hash = "f2c61fbe782d2519849f330457ad92e11da926af856aaa73223a60e5d58c73c7"
	salt = "0000000000000000000301e2801a9a9598bfb114e574a91a887f2132f33047e6"
	gameId = 7182537

	get_crash_history(hash, salt, gameId, 100000)


