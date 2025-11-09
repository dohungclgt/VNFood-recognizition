
# VNFood Recognition

VNFood Recognition là hệ thống nhận dạng hình ảnh được thiết kế để nhận diện và phân loại các món ăn Việt Nam. Dự án sử dụng các mô hình học sâu để xử lý hình ảnh món ăn và đưa ra tên món ăn dự đoán kèm theo điểm tin cậy. Dự án này có thể được sử dụng trong các ứng dụng như nhận diện món ăn trong các ứng dụng di động hoặc hệ thống phân loại món ăn.

## Mục lục

- [Tổng quan](#tổng-quan)
- [Cài đặt](#cài-đặt)
- [Cách sử dụng](#cách-sử-dụng)
- [Đóng góp](#đóng-góp)
- [Giấy phép](#giấy-phép)
- [Liên hệ](#liên-hệ)

## Tổng quan

VNFood Recognition được xây dựng bằng các kỹ thuật học máy hiện đại, sử dụng các mạng nơ-ron tích chập (CNN) và sử dụng Google Vision API để phân tích hình ảnh các món ăn. Hệ thống này đã được huấn luyện trên một bộ dữ liệu các món ăn Việt Nam, giúp nó dự đoán chính xác các món ăn từ hình ảnh. 

## Tính năng

- Phân loại hình ảnh các món ăn Việt Nam với độ chính xác cao.
- Cung cấp điểm tin cậy cho các dự đoán.
- Giao diện dễ sử dụng để tích hợp mô hình vào ứng dụng.
- Được xây dựng bằng các thư viện học sâu phổ biến như TensorFlow/PyTorch (tùy thuộc vào thư viện được sử dụng).
- Cung cấp kết quả: độ chính xác, mô tả món ăn, cách chế biến và cách thưởng thức

## Cài đặt

Để bắt đầu sử dụng hệ thống VNFood Recognition, hãy làm theo các bước dưới đây:

### Yêu cầu

- Python 3.x
- pip (trình cài đặt gói Python)
- TensorFlow/PyTorch (tùy thuộc vào thư viện được sử dụng)
- Google Vision API (https://aistudio.google.com/api-keys)

### Bước 1: Clone repository

```bash
git clone https://github.com/dohungclgt/VNFood-recognizition.git
cd VNFood-recognizition
```

### Bước 2: Cài đặt các thư viện phụ thuộc

Tạo môi trường ảo (khuyến khích nhưng không bắt buộc):

```bash
python -m venv venv
source venv/bin/activate  # Trên Windows sử dụng 'venv\Scripts\activate'
```

Cài đặt các gói Python cần thiết:

```bash
pip install -r requirements.txt
```

### Bước 3: Chuẩn bị API

Truy cập vào: https://aistudio.google.com/api-keys và dán API key của bạn vào thư mục:
```bash
.streamlit/secrets.toml
```
Dán key của bạn vào dòng code này
```toml
[general]
GOOGLE_API_KEY = "API key here"
```

### Bước 4: Chạy hệ thống

Để chạy ứng dụng, chạy theo dòng lệnh này ở Command Prompt hoặc Terminal trên VSCode:

```bash
streamlit run app.py
```

Lệnh này sẽ chạy localhost, việc của mình chỉ cần chọn ngôn ngữ, vùng miền, upload ảnh món ăn và ấn phân tích.


## Đóng góp

Nếu bạn muốn đóng góp vào dự án VNFood Recognition, hãy fork repository và gửi pull request. Vui lòng làm theo các hướng dẫn sau:

1. Fork repository.
2. Tạo một nhánh tính năng (feature branch).
3. Viết các bài kiểm tra để đảm bảo các thay đổi của bạn hoạt động đúng.
4. Gửi pull request với mô tả rõ ràng về những gì bạn đã làm.

## Giấy phép

Có thể dùng để tham khảo cách làm. Có thể sử dụng như là project của riêng mình

## Liên hệ

Nếu bạn có bất kỳ câu hỏi nào hoặc cần thêm sự hỗ trợ, đừng ngần ngại liên hệ với mình:

- **Tên**: dohungclgt
- **GitHub**: https://github.com/dohungclgt
