#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

NUMBER_OF_TESTS = 10_000
LENGTH_OF_TESTS = 100
RANDOM_RANGE = 1_000_000


rng = np.random.default_rng(12345)
values = rng.integers(-RANDOM_RANGE, +RANDOM_RANGE, (NUMBER_OF_TESTS,LENGTH_OF_TESTS))

# range restriction
lower_bounds = np.maximum.accumulate(values-RANDOM_RANGE, axis=1)
upper_bounds = np.minimum.accumulate(values+RANDOM_RANGE, axis=1)
ranges = upper_bounds-lower_bounds

# sort them to get percentiles
sorted_ranges = np.sort(ranges, axis=0)

for i in range(10):
    plt.plot(sorted_ranges[round(NUMBER_OF_TESTS/10. * i)])
plt.plot(sorted_ranges[-1])
plt.ylabel('size of range')
plt.xlabel('number of random positions')
plt.savefig('range-restricting.svg')
plt.close()


# averaging

# cumulative sum inside each test
cumulative_sums = np.cumsum(values, axis=1)

# then compute the average by dividing the cumulative sum by the number of values up until that point
averages = cumulative_sums / np.fromfunction(lambda x: x+1, (LENGTH_OF_TESTS,))

# sort them to get percentiles
sorted_averages = np.sort(np.abs(averages), axis=0)

for i in range(10):
    plt.plot(sorted_averages[round(NUMBER_OF_TESTS/10. * i)])
plt.plot(sorted_averages[-1])
plt.ylabel('distance from 0')
plt.xlabel('number of random positions')
plt.savefig('averaging.svg')

