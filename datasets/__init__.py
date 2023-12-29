"""
Generate a random linear regression dataset
Author: Son Phat Tran
"""
import numpy as np
import matplotlib.pyplot as plt


# Generate some random points X uniformly
X = np.random.uniform(0, 10, 30)

# True linear function
m0 = 1
m1 = 2

# Generate label
beta = 0.5
t = m0 + m1 * X + np.random.normal(loc=0, scale=1/beta, size=30)


if __name__ == "__main__":
    # Plot the values
    plt.scatter(X, t)
    plt.show()
