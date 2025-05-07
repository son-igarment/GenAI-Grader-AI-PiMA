# GenAI Grader AI (PiMA)

Automated grading system for generative AI and numerical methods assignments.

## Information

- **Author:** Phạm Lê Ngọc Sơn
- **Email:** son.phamlengoc@gmail.com
- **Version:** 1.0.0

## Project Description

The "GenAI Grader AI (PiMA)" project is an automated grading system for assignments on generative AI and numerical methods. The system was developed to help instructors and students evaluate assignments on Monte Carlo methods, Importance Sampling techniques, and other numerical computation algorithms.

## Project Structure

```
GenAI-Grader-AI-PiMA/
├── .git/                      # Git directory
├── grader_homework_2/         # Homework 2 grader
│   ├── __init__.py            # Module initialization file
│   ├── grade_all.py           # Script to grade all assignments
│   ├── grade_p1.py            # Script to grade problem 1
│   ├── grade_p2.py            # Script to grade problem 2
│   ├── grade_p3.py            # Script to grade problem 3
│   ├── grade_p4.py            # Script to grade problem 4
│   ├── optimize_for_final_grading.py # Optimization for final grading
│   ├── plot_approximation.py  # Approximation plotting
│   └── requirements.txt       # Required libraries
│
├── grader_homework_3/         # Homework 3 grader
│   ├── __init__.py            # Module initialization file
│   ├── grade_p1.py            # Script to grade problem 1
│   ├── grade_p2.py            # Script to grade problem 2
│   ├── grade_p3.py            # Script to grade problem 3
│   ├── dual_number.py         # Dual Numbers implementation
│   ├── function.npy           # Grading data
│   ├── U.npy                  # U matrix for SVD
│   ├── V.npy                  # V matrix for SVD
│   ├── Z.npy                  # Z matrix
│   └── requirements.txt       # Required libraries
│
├── .gitignore                 # Files excluded from Git
├── .gitattributes             # Git attributes
└── README.md                  # This guide
```

## Main Features

### Grader Homework 2
- Grading assignments on Monte Carlo methods
- Evaluating Importance Sampling techniques
- Testing sampling optimization methods

### Grader Homework 3
- Evaluating Dual Numbers performance
- Grading function approximation techniques
- Performing SVD (Singular Value Decomposition) checks

## Usage

### Requirements

1. Python 3.8 or higher
2. Libraries listed in the requirements.txt file for each homework

### Installation

```bash
# Clone the project (if not already available)
git clone https://github.com/your-username/GenAI-Grader-AI-PiMA.git
cd GenAI-Grader-AI-PiMA

# Install libraries for Homework 2
pip install -r grader_homework_2/requirements.txt

# Install libraries for Homework 3
pip install -r grader_homework_3/requirements.txt
```

### Grading Homework 2

```python
from grader_homework_2.grade_all import grade_all

# Call the grading function with the functions/classes to be graded
grade_all(
    sample_needle,
    is_lie_across,
    ImportanceSampling,
    in_square_pdf,
    pdf_IS,
    better_sampling_IS,
    better_pdf_IS,
    is_logging=True  # Set to True to display detailed grading process
)
```

### Grading Homework 3

```python
# Grade part 1
from grader_homework_3.grade_p1 import grade as grade_p1
result_p1 = grade_p1(
    your_function_p1,
    is_logging=True
)

# Grade part 2
from grader_homework_3.grade_p2 import grade as grade_p2
result_p2 = grade_p2(
    your_function_p2,
    is_logging=True
)

# Grade part 3
from grader_homework_3.grade_p3 import grade as grade_p3
result_p3 = grade_p3(
    your_function_p3,
    is_logging=True
)
```

## Contact and Contributions

If you have any questions or suggestions, please contact:
- **Email:** son.phamlengoc@gmail.com
- **GitHub Issues:** Create a new issue in the repository

## License

© 2023 Phạm Lê Ngọc Sơn. All rights reserved.