# GenAI Grader AI (PiMA)

Hệ thống tự động chấm điểm bài tập về AI tạo sinh và các phương pháp số học.

## Thông tin

- **Tác giả:** Phạm Lê Ngọc Sơn
- **Email:** son.phamlengoc@gmail.com
- **Phiên bản:** 1.0.0

## Mô tả dự án

Dự án "GenAI Grader AI (PiMA)" là một hệ thống tự động chấm điểm bài tập về AI tạo sinh và các phương pháp số học. Hệ thống được phát triển nhằm giúp giảng viên và sinh viên có thể đánh giá các bài tập về phương pháp Monte Carlo, kỹ thuật lấy mẫu (Importance Sampling), và các thuật toán tính toán số học khác.

## Cấu trúc dự án

```
GenAI-Grader-AI-PiMA/
├── .git/                      # Thư mục Git
├── grader_homework_2/         # Bộ chấm điểm bài tập 2
│   ├── __init__.py            # File khởi tạo module
│   ├── grade_all.py           # Script chấm tất cả bài tập
│   ├── grade_p1.py            # Script chấm bài 1
│   ├── grade_p2.py            # Script chấm bài 2
│   ├── grade_p3.py            # Script chấm bài 3
│   ├── grade_p4.py            # Script chấm bài 4
│   ├── optimize_for_final_grading.py # Tối ưu hóa việc chấm điểm
│   ├── plot_approximation.py  # Vẽ đồ thị xấp xỉ
│   └── requirements.txt       # Các thư viện cần thiết
│
├── grader_homework_3/         # Bộ chấm điểm bài tập 3
│   ├── __init__.py            # File khởi tạo module
│   ├── grade_p1.py            # Script chấm bài 1
│   ├── grade_p2.py            # Script chấm bài 2
│   ├── grade_p3.py            # Script chấm bài 3
│   ├── dual_number.py         # Implementation của Dual Numbers
│   ├── function.npy           # Dữ liệu chấm điểm
│   ├── U.npy                  # Ma trận U cho SVD
│   ├── V.npy                  # Ma trận V cho SVD
│   ├── Z.npy                  # Ma trận Z
│   └── requirements.txt       # Các thư viện cần thiết
│
├── .gitignore                 # Các file được loại trừ khỏi Git
├── .gitattributes             # Thuộc tính Git
└── README.md                  # File hướng dẫn (đang đọc)
```

## Chức năng chính

### Grader Homework 2
- Chấm điểm các bài tập về phương pháp Monte Carlo
- Đánh giá kỹ thuật Importance Sampling
- Kiểm tra các phương pháp tối ưu hóa sampling

### Grader Homework 3
- Đánh giá hiệu suất của Dual Numbers
- Chấm điểm các kỹ thuật xấp xỉ hàm số
- Thực hiện kiểm tra SVD (Singular Value Decomposition)

## Cách sử dụng

### Yêu cầu cài đặt

1. Python 3.8 trở lên
2. Các thư viện trong file requirements.txt của mỗi homework

### Cài đặt

```bash
# Clone dự án về máy (nếu chưa có)
git clone https://github.com/your-username/GenAI-Grader-AI-PiMA.git
cd GenAI-Grader-AI-PiMA

# Cài đặt thư viện cho Homework 2
pip install -r grader_homework_2/requirements.txt

# Cài đặt thư viện cho Homework 3
pip install -r grader_homework_3/requirements.txt
```

### Chấm điểm bài tập 2

```python
from grader_homework_2.grade_all import grade_all

# Gọi hàm chấm điểm với các tham số là các hàm/lớp cần chấm
grade_all(
    sample_needle,
    is_lie_across,
    ImportanceSampling,
    in_square_pdf,
    pdf_IS,
    better_sampling_IS,
    better_pdf_IS,
    is_logging=True  # Đặt True để hiển thị chi tiết quá trình chấm
)
```

### Chấm điểm bài tập 3

```python
# Chấm điểm phần 1
from grader_homework_3.grade_p1 import grade as grade_p1
result_p1 = grade_p1(
    your_function_p1,
    is_logging=True
)

# Chấm điểm phần 2
from grader_homework_3.grade_p2 import grade as grade_p2
result_p2 = grade_p2(
    your_function_p2,
    is_logging=True
)

# Chấm điểm phần 3
from grader_homework_3.grade_p3 import grade as grade_p3
result_p3 = grade_p3(
    your_function_p3,
    is_logging=True
)
```

## Liên hệ và đóng góp

Nếu bạn có bất kỳ câu hỏi hoặc đề xuất nào, vui lòng liên hệ:
- **Email:** sonnguyen@example.com (thay thế bằng email thật của bạn)
- **GitHub Issues:** Tạo issue mới trong repository

## Giấy phép

© 2023 Phạm Lê Ngọc Sơn. Tất cả các quyền được bảo lưu.