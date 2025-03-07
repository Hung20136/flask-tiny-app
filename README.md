# Flask Tiny App

## 1. Thông tin cá nhân
- **Họ tên**: Lê Nguyễn Phúc Hưng
- **Mã sinh viên**: 22672481
- **Họ tên**: Phạm Hoàng Phát
- **Mã sinh viên**: 22703861
## 2. Mô tả project
Ứng dụng web đơn giản với Flask gồm 2 chức năng chính:
- Blog: Cho phép user tạo, chỉnh sửa, xóa bài viết.
- To-do list: User có thể quản lý danh sách công việc cá nhân.

## 3. Hướng dẫn cài đặt & chạy
### Yêu cầu:
-Python 3.12
-PostgreSQL
-Git
-Docker

### Cài đặt & chạy:
```bash
git clone https://github.com/Hung20136/flask-tiny-app.git
cd flask-tiny-app
```

### Thiết lập môi trường
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Cài đặt cần thiết
```bash
pip install -r requirements.txt
```
### Lệnh để khởi tạo
```bash
flask run
```
Ứng dụng sẽ có tại địa chỉ: **`http://127.0.0.1:5000`**

## 🐳 Triển khai với Docker
```bash
docker build -t flask-tiny-app .
docker run -p 5000:5000 flask-tiny-app
```

