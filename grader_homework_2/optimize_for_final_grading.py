"""
Grading Optimizer for Final Assessment
GenAI Grader AI (PiMA) - Homework 2
Author: Phạm Lê Ngọc Sơn
Version: 1.0.0
Copyright © 2023 Phạm Lê Ngọc Sơn. All rights reserved.
"""

class GradingOptimizer:
    """
    A class to optimize grading process for final assessment.
    Controls the behavior of certain functions during final grading.
    """
    is_optimized_for_final_grading = False

    @classmethod
    def optimize_for_final_grading(cls, state: bool = True):
        """
        Sets the optimization state for final grading.
        
        Args:
            state (bool): Whether to optimize for final grading.
        """
        cls.is_optimized_for_final_grading = state
