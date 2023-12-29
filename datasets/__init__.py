"""
Generate a random linear regression dataset
Author: Son Phat Tran
"""
import numpy as np
import matplotlib.pyplot as plt


# Generate some random points X uniformly
N = 5
X = np.random.uniform(0, 10, N)
X = np.sort(X)

# True linear function
m0 = 1
m1 = 2

# Generate label
beta = 0.5
t = m0 + m1 * X + np.random.normal(loc=0, scale=1/beta, size=N)


if __name__ == "__main__":
    # Plot the values
    plt.scatter(X, t)
    plt.show()
