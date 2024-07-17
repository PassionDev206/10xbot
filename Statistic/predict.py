
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


def main(th, n_trial, data_path):
    """
    Run this function with a given threshold.
    If you wish, reset the prob_density of the gambler
    """
    assert(th>1 and th<11)

    train_data = np.loadtxt(data_path).ravel()
    
    prob_den, bins = compute_distribution(train_data)

    gambler = Gambler(prob_den, bins)
    
    np.random.seed(1989) # remove if you wish
    result_arr = []
    for i in range(n_trial):
        prediction = gambler.toss_coin(th)
        # print(prediction)
        result_arr.append(prediction)
    result_arr = np.array(result_arr)
    np.savetxt("real_test_V1_20000.txt", result_arr, fmt="%.0f")
        

if __name__ == "__main__":
    T = 2   # We bet on 2X
    N = 10000  # We will play with 10 trials. The bigger, The better!
    data_path = "train_data.txt"

    main(
        th=T,
        n_trial=N,
        data_path=data_path
    )