"""
Plot Approximation Utility for Monte Carlo Methods
GenAI Grader AI (PiMA) - Homework 2
Author: Phạm Lê Ngọc Sơn
Version: 1.0.0
Copyright © 2023 Phạm Lê Ngọc Sơn. All rights reserved.
"""

import matplotlib.pyplot as plt
import random
from typing import *
import numpy as np
from tqdm import tqdm
from .optimize_for_final_grading import GradingOptimizer

def plot_approximation(
    student_id: Any,
    approx_func: Callable[[], float],
    tqdm_desc: str,
    var_name: str,
    true_value: Any,
    method_name: str,
    num_trials: int
):
    if GradingOptimizer.is_optimized_for_final_grading:
        print("This function has been optimized for final grading. Cannot run this function.")
        return
    
    random.seed(student_id)

    approximations = [
        approx_func()
        for _ in tqdm(range(num_trials), desc=tqdm_desc)
    ]

    # Compute sample mean and variance
    sample_mean = np.mean(approximations)
    sample_variance = np.var(approximations, ddof=1)

    # Plot histogram
    plt.figure(figsize=(10, 6))
    plt.hist(approximations, bins=30, color='blue', edgecolor='black', alpha=0.7)
    plt.axvline(x=sample_mean, color='green', linestyle='dashed', linewidth=2, label=f"Sample Mean: {sample_mean:.5f}")
    plt.axvline(x=true_value, color='red', linestyle='dashed', linewidth=2, label=f"True Value of {var_name}: {true_value:.5f}")
    plt.xlabel(f"Approximated {var_name} Value")
    plt.ylabel("Frequency")
    plt.title(f"Distribution of {var_name} Approximation using {method_name}\nSample Mean: {sample_mean:.5f}, Sample Variance: {sample_variance:.5f}")
    plt.legend()
    plt.show()