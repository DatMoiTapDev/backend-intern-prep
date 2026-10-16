# Practice Day 3: Xử lý dữ liệu phức tạp và Hệ thống Monitor

## 🎯 Mục tiêu
Làm quen với các kỹ thuật thao tác dữ liệu nâng cao: cắt chuỗi, truy xuất từ điển lồng nhau (Nested Dict) mô phỏng API trả về, thuật toán đếm (Aggregation) và kiểm tra lỗi hàng loạt.

## 📝 Đề bài
**Bài 1: Xử lý chuỗi rác (String Split)**
Dùng lệnh `.split()` để tách một chuỗi chứa nhiều IP cách nhau bằng dấu phẩy thành một List. Sau đó lọc ra các IP bắt đầu bằng "192.".

**Bài 2: Phân tích dữ liệu JSON (Nested Dictionary)**
Truy xuất vào một cấu trúc Dictionary nhiều lớp (mô phỏng dữ liệu từ AWS trả về) để lấy ra ID của các máy chủ đang "running".

**Bài 3: Thuật toán Thống kê (Aggregation)**
Duyệt qua danh sách hàng chục máy chủ. Đếm xem có bao nhiêu máy đang "online" và bao nhiêu máy "offline", sau đó in kết quả tổng kết.

**Bài 4: Kiểm tra dữ liệu hàng loạt (Try-Except với Vòng lặp)**
Duyệt qua một danh sách các cổng (Port). Dùng `try...except ValueError` để ép kiểu dữ liệu về số nguyên (`int`). Bắt lỗi nếu có dữ liệu chứa chữ cái.

**Bài 5: OOP - Xây dựng hệ thống Giám sát (Monitor)**
Tạo `class Server` chứa trạng thái. Tạo `class SystemMonitor` chứa danh sách Server, có khả năng quét toàn bộ hệ thống để tìm và cảnh báo tên những Server đang bị "offline".
