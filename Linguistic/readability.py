from readability_score.calculators.fleschkincaid import FleschKincaid
# Download from https://github.com/wimmuskee/readability-score
import pandas as pd
import numpy as np
from loadRandom import loadRandom2
import matplotlib.pyplot as plt
import numpy_indexed as npi
import seaborn as sns

# ----------------------
# Readability Analysis
# Calculates the readability score for the sample, and plots a scatter plot of the mean
# reading ages
# ----------------------
# REQUIRES:
#   - FleschKincaid calculator from https://github.com/wimmuskee/readability-score
#   - loadRandom file from the repository
# ----------------------

if __name__ == '__main__':
    seed = 2
    data = loadRandom2(
        '/Users/caitchison/Documents/Yelp/yelp_dataset/restaurants_only.csv', 1e5, seed, 3778803).loc[
            :, ('stars_x', 'text', 'useful', 'cool', 'funny', 'date')]

    # Get metric and mask
    usefulness = np.array(data.useful)
    mask = usefulness > 0
    usefulness = usefulness[mask]

    # Get readability score using FleischKincaid
    reviews = np.array(data.text)[mask]
    minAge = np.array([FleschKincaid(text).min_age for text in reviews])
    mask = minAge > 0
    minAge = minAge[mask]
    usefulness = usefulness[mask]

    # Calculate Average Values
    x = minAge
    x_unique, y_mean = npi.group_by(x).mean(usefulness)
    mask = x_unique < 25
    x_unique = x_unique[mask]
    y_mean = y_mean[mask]

    # Plot graph
    sns.set()

    sns.scatterplot(x_unique, y_mean)
    plt.ylabel('Usefulness Count (mean)')

    plt.subplot(2, 1, 2)
    plt.xlabel('Minimum Reading Age (FK)')

    plt.show()
