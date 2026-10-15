# Practice Day 2: Xử lý Chuỗi, Lọc nhiều điều kiện và Bắt lỗi

## 🎯 Mục tiêu
Luyện tập các kỹ năng xử lý Log, cập nhật dữ liệu linh hoạt, sử dụng toán tử Logic và kỹ thuật bảo vệ hệ thống không bị crash (Try...Except).

## 📝 Đề bài
**Bài 1: Phân tích Log hệ thống**
Duyệt qua danh sách system logs. Dùng toán tử `in` để lọc và in ra màn hình những dòng log có chứa từ khóa `"ERROR"`.

**Bài 2: Cấu hình Firewall (Thêm/Sửa/Xóa)**
Cho dictionary chứa các port đang mở `firewall_ports = {"SSH": 22, "HTTP": 80, "HTTPS": 443}`. Thực hiện:
- Thêm port "MySQL": 3306.
- Cập nhật port "HTTP" thành 8080.
- Xóa port "SSH" khỏi danh sách.

**Bài 3: Lọc dữ liệu nhiều điều kiện**
Cho danh sách cấu hình server. Dùng toán tử `and` để tìm và in ra tên những server thỏa mãn cả 2 điều kiện: đang `"online"` và có lượng RAM >= 1024.

**Bài 4: Bắt lỗi hệ thống (Try...Except)**
Cố gắng truy xuất một Key không tồn tại (`password`) từ Dictionary cấu hình Database. Dùng `try...except KeyError` để hứng lỗi, in ra thông báo cảnh báo, đảm bảo chương trình không bị crash và vẫn chạy tới dòng code cuối cùng.

**Bài 5: OOP - Load Balancer**
Xây dựng `class Server` có chức năng đếm số lượng request. Xây dựng `class LoadBalancer` có khả năng lưu trữ các Object Server và chứa hàm `phan_bo_tai()` để gọi hàm xử lý request của tất cả Server đang nằm trong danh sách quản lý.
