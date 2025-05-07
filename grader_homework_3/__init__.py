"""
GenAI Grader AI (PiMA) - Homework 3 Grader
Author: Phạm Lê Ngọc Sơn
Version: 1.0.0
Copyright © 2023 Phạm Lê Ngọc Sơn. All rights reserved.
"""

from .grade_p1 import grade as grade_p1
from .grade_p2 import grade as grade_p2
from .grade_p3 import grade as grade_p3
from .dual_number import DualNumber

__all__ = [
    'grade_p1',
    'grade_p2',
    'grade_p3',
    'DualNumber'
]
