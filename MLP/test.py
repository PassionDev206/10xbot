import numpy as np
from sklearn.preprocessing import StandardScaler

# Example time-series data with 1000 samples, each with 50 time steps and 10 features
data = np.random.rand(1000, 50, 10)

# Flatten the data for MLP input
flattened_data = data.reshape(data.shape[0], -1)
print(flattened_data)
# Standardize the data
scaler = StandardScaler()
standardized_data = scaler.fit_transform(flattened_data)

# Assuming a batch size of 32
batch_size = 32
num_batches = len(standardized_data) // batch_size

for i in range(num_batches):
    batch_data = standardized_data[i * batch_size: (i + 1) * batch_size]
    # Feed batch_data into the MLP model
    # model.fit(batch_data, ...)

print(batch_data)