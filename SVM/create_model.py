import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Create a synthetic dataset
np.random.seed(42)
X = np.random.randn(100, 2)  # 100 samples, 2 features
y = np.random.randint(0, 2, 100)  # Binary target variable

print(X)

print(y)

# # Convert to DataFrame for convenience
# df = pd.DataFrame(X, columns=['feature1', 'feature2'])
# df['target'] = y

# # Separate features and target
# X = df[['feature1', 'feature2']]
# y = df['target']

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# # Standardize the features
# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

# # Train the SVM model
# svm_model = SVC(kernel='linear')  # You can try other kernels like 'rbf', 'poly', etc.
# svm_model.fit(X_train, y_train)

# # Make predictions
# y_pred = svm_model.predict(X_test)

# # Evaluate the model
# accuracy = accuracy_score(y_test, y_pred)
# print(f'Accuracy: {accuracy:.2f}')

# # Detailed classification report
# print('Classification Report:')
# print(classification_report(y_test, y_pred))

# # Confusion matrix
# print('Confusion Matrix:')
# print(confusion_matrix(y_test, y_pred))
