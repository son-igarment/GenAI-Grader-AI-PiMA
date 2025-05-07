from .grade_p1 import grade as grade_p1
from .grade_p2 import grade as grade_p2
from .grade_p3 import grade as grade_p3
from .grade_p4 import grade as grade_p4
from IPython.core.display import display_html, HTML
from string import Template
import numpy as np

def grade_all(
    sample_needle,
    is_lie_across,
    ImportanceSampling,
    in_square_pdf,
    pdf_IS,
    better_sampling_IS,
    better_pdf_IS,
    is_logging = False
):
    try:
      result_p1 = grade_p1(
        sample_needle,
        is_lie_across,
        is_logging
      )
    except Exception as e:
      result_p1 = 0
      print(f"Error grading Problem 1: {e}")

    try:
      result_p2 = grade_p2(
        ImportanceSampling,
        is_logging
      )
    except Exception as e:
      result_p2 = 0
      print(f"Error grading Problem 2: {e}")

    try:
      result_p3 = grade_p3(
        ImportanceSampling,
        in_square_pdf,
        pdf_IS,
        is_logging
      )
    except Exception as e:
      result_p3 = 0
      print(f"Error grading Problem 3: {e}")

    try:
      result_p4 = grade_p4(
        ImportanceSampling,
        better_sampling_IS,
        better_pdf_IS,
        is_logging
      )
    except Exception as e:
      result_p4 = 0
      print(f"Error grading Problem 4: {e}")

    html_template = Template("""
<div style="font-family: 'Segoe UI', sans-serif; max-width: 500px; margin: 20px auto; border-radius: 12px; box-shadow: 0 6px 15px rgba(0,0,0,0.15); overflow: hidden;">
  <div style="background: linear-gradient(to right, #ff6a00, #ee0979); color: white; padding: 20px;">
    <h2 style="margin: 0; font-size: 26px;">🔥 Assignment Results</h2>
    <p style="margin: 5px 0 0; font-size: 14px;">Phạm Lê Ngọc Sơn | GenAI Grader AI (PiMA)</p>
  </div>
  <div style="background: white; padding: 20px;">
    <table style="width: 100%; border-collapse: collapse; font-size: 16px; color: #333;">
      <tr>
        <td style="padding: 12px; border-bottom: 1px solid #ddd;">Problem 1</td>
        <td style="padding: 12px; border-bottom: 1px solid #ddd; text-align: right;"><strong>$score1</strong></td>
      </tr>
      <tr>
        <td style="padding: 12px; border-bottom: 1px solid #ddd;">Problem 2</td>
        <td style="padding: 12px; border-bottom: 1px solid #ddd; text-align: right;"><strong>$score2</strong></td>
      </tr>
      <tr>
        <td style="padding: 12px; border-bottom: 1px solid #ddd;">Problem 3</td>
        <td style="padding: 12px; border-bottom: 1px solid #ddd; text-align: right;"><strong>$score3</strong></td>
      </tr>
      <tr>
        <td style="padding: 12px; border-bottom: 1px solid #ddd;">Problem 4</td>
        <td style="padding: 12px; border-bottom: 1px solid #ddd; text-align: right;"><strong>$score4</strong></td>
      </tr>
      <tr style="background-color: #ffe57f; font-weight: bold;">
        <td style="padding: 12px;">Total Score</td>
        <td style="padding: 12px; text-align: right;">🎯 <strong>$scorefinal</strong></td>
      </tr>
    </table>
  </div>
  <div style="background: #f5f5f5; padding: 12px; text-align: center; font-size: 12px; color: #777;">
    © 2023 Phạm Lê Ngọc Sơn. All rights reserved.
  </div>
</div>
"""). substitute(
        score1 = f"{int(result_p1 * 100)}%" if result_p1 is not None else f"Not graded",
        score2 = f"{int(result_p2 * 100)}%" if result_p2 is not None else f"Not graded",
        score3 = f"{int(result_p3 * 100)}%" if result_p3 is not None else f"Not graded",
        score4 = f"{int(result_p4 * 100)}%" if result_p4 is not None else f"Not graded",
        scorefinal = f"{np.mean([result for result in [result_p1, result_p2, result_p3, result_p4] if result is not None]) * 100:.2f}%"
    )

    display_html(HTML(html_template))
