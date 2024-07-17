
"""
Model V1: always bet for a fixed threshold, with a fixed probability.
    See the Doc file for a detailed explanation.
To make a prediction call the "main" function.
We produce a single digit at each trial, given T.
    * If the digit is zero, don't bet.
    * If the digit is one, bet for T.
"""
import numpy as np


def compute_distribution(indata):
    """
    Given a long sequence, make a histogram of all data
    """
    bins1 = np.linspace(1, 10, 10)
    bins2 = np.arange(2,7)
    bins = np.concatenate((bins1, np.power(10, bins2)))
    print("bins = ", bins)
    freq, _ = np.histogram(indata.ravel(), bins=bins, density=False)
    prob_density = freq/np.sum(freq)
    print("Prob density: ", prob_density)
    return prob_density, bins

def get_cum_prob (prob_density, bins, thres):
    """
    Return the cumulative probability: P(x<thres), where
    * prob_density = p(x)
    * thres = threshold
    One may use np.cumsum but just in case of any value of thres!!!
    """
    args = np.argwhere(bins<=thres).ravel()
    if len(args)==0:
        return 0
    else:
        arg = args[-1]
        return np.sum(prob_density[:arg])


class Gambler:
    def __init__(self, prob_density, bins):
        self.prob_density = prob_density
        self.bins = bins
        self.choice_arr = np.array([0, 1], dtype=int)

    def set_density(self, new_density, new_bins):
        self.prob_density = new_density
        self.bins = new_bins

    def toss_coin(self, thres): 
        prob = get_cum_prob(self.prob_density, self.bins, thres)
        prob_arr = np.array([prob, 1.-prob])

        return np.random.choice(self.choice_arr, p=prob_arr)

if __name__ == "__main__":
    threshold = 3   # We bet on 2X
    train_data_path = "train_data.txt"
    test_data_path = "test_data.txt"

    train_data = np.loadtxt(train_data_path).ravel()
    test_data = np.loadtxt(test_data_path).ravel()

    predictions = []

    assert(threshold>1 and threshold<11)
    np.random.seed(1989)

    for i in range(3000):
        if i > 0:
            train_data = np.append(train_data, test_data[i - 1])
        prob_den, bins = compute_distribution(train_data)
        gambler = Gambler(prob_den, bins)
        prediction = gambler.toss_coin(threshold)
        predictions.append(prediction)
    
    predictions = np.array(predictions)
    np.savetxt("prediction_result.txt", predictions, fmt="%.0f")