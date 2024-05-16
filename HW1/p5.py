import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb

def P_function(n):
    result = 0
    for k in range(109):
        result += (-1)**k * comb(108, k) * ((108 - k) / 108)**n
    return result

n_values = np.arange(200, 1001)
P_values = [P_function(n) for n in n_values]

# 寻找第一次P值大于0.95的n值
first_index_above_095 = next((i for i, p in enumerate(P_values) if p > 0.95), None)
n_value_above_095 = n_values[first_index_above_095]

plt.figure(figsize=(10, 6))
plt.plot(n_values, P_values, color='blue', linestyle='-')
plt.scatter(n_value_above_095, P_values[first_index_above_095], color='red', label=f'n={n_value_above_095}')
plt.xlabel('n', fontsize=14)
plt.ylabel('P', fontsize=14)
plt.title('Graph of P for n in the range [200, 1000]', fontsize=16)
plt.grid(True)
plt.legend()
plt.show()

print(f"The first time P > 0.95 occurs at n = {n_value_above_095}")
