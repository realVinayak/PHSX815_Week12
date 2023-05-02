import numpy as np
import math
import matplotlib.pyplot as plt

mean_list = [1, 5]
weight_list = [0.4, 0.6]
N_sample = 1000
H = 2.0

def standard_gaussian(mean, std_dev, x):
    denom = 1 / (std_dev * math.sqrt(2 * math.pi))
    numer = math.exp(-1/2 * (math.pow((x - mean) / std_dev, 2)))
    return denom * numer


def mixed_gaussian_prob(means, probs, x):
    prob = 0
    for counter in range(len(means)):
        prob += standard_gaussian(means[counter], 1, x)*probs[counter]
    return prob


def generate_multimodal_data():
    samples = []
    for sample_counter in range(N_sample):
        mean = np.random.choice(mean_list, p=weight_list)
        samples.append(np.random.normal(mean, 1))
    return samples

def get_gaussian_estimate(point_to_eval, data_points, h):
    estimates = [standard_gaussian(point_to_eval, h, data_point) for data_point in data_points]
    return sum(estimates)/len(data_points)


def main():
    generated_samples = generate_multimodal_data()
    generated_samples.sort()
    plt.hist(generated_samples, label='Simulated Values', bins=100, density=True, alpha=0.6)
    final_values = [mixed_gaussian_prob(mean_list, weight_list, x) for x in generated_samples]
    predicted_values = [get_gaussian_estimate(point, generated_samples, H) for point in generated_samples]
    plt.plot(generated_samples, final_values, label='True Values', linewidth=6)
    plt.plot(generated_samples, predicted_values, label='Predicted Values', linewidth=4)
    plt.legend()
    plt.savefig(f'histogram_generated_h_{H}.png')


if __name__ == '__main__':
    main()
