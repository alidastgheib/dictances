import numpy as np
from scipy.stats import chisquare

def chi_square_distance(repr1: np.ndarray, repr2: np.ndarray) -> float:
    repr1.tolist()
    repr2.tolist()
    dist_sum = 0

    for x in range(max(len(repr1), len(repr2))):
        val1 = 0
        val2 = 0

        try:
            val1 = repr1[x]
        except IndexError:
            pass

        try:
            val2 = repr2[x]
        except IndexError:
            pass

        dist_sum += chisquare([val1,val2])[0]
    return dist_sum