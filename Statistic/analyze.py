import numpy as np

def analyze_result(predictions, actual):
    correct_number = 0
    wrong_number = 0
    total_upper_number = 0
    for i in range(len(predictions)):
        if predictions[i] > 0:
            total_upper_number += 1
            if actual[i] >= 3:
                correct_number += 1
            else:
                wrong_number += 1
    
    print(total_upper_number)
    print(correct_number)
    print(wrong_number)
    accuracy = correct_number / total_upper_number * 100
    print(f"Accuracy: {accuracy}%")

    profit = correct_number * 3 - total_upper_number
    print(f"Profit: {profit}")

if __name__ == "__main__":
    # load the prediction result file
    pred_path = "prediction_result.txt"
    predictions = np.loadtxt(pred_path).ravel()

    # load the actual data file
    actual_path = "test_data.txt"
    actual = np.loadtxt(actual_path).ravel()

    analyze_result(predictions, actual)
