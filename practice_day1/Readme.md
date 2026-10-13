# Practice Day 1: Bài tập Thực hành Tổng hợp

## 🎯 Mục tiêu
Củng cố nền tảng Python (List, Dict, Loop, Function, OOP) thông qua 5 kịch bản thực tế của kỹ sư Backend/DevOps.

## 📝 Đề bài
**Bài 1: Lọc dữ liệu mảng**
Duyệt qua danh sách IP `["192.168.1.1", "8.8.8.8", "10.0.0.5", "192.168.1.100", "1.1.1.1"]`. In ra những IP thuộc mạng nội bộ (bắt đầu bằng "192.168.").

**Bài 2: Thao tác Dictionary**
Cho biến `server_hien_tai = {"name": "DB-Main", "status": "offline", "cpu": "99%"}`. Viết hàm `khoi_dong_lai(thiet_bi)` để truy cập vào từ điển, đổi `status` thành "online" và `cpu` thành "10%". In kết quả ra màn hình.

**Bài 3: Tìm kiếm Server yếu nhất**
Cho list chứa dict thông tin 3 server. Viết thuật toán vòng lặp so sánh để tìm ra cấu hình Server có lượng RAM nhỏ nhất và in ra thông báo yêu cầu cấp thêm RAM.

**Bài 4: OOP Phân quyền hệ thống**
Tạo `class TaiKhoan` nhận `username` và `role`. Viết hàm kiểm tra: nếu role là "admin" thì cho phép xóa Database, nếu là "user" thì chỉ được xem dữ liệu.

**Bài 5: OOP Kế thừa - Cảnh báo hệ thống**
Tạo class cha `CanhBao`. Tạo 2 class con `EmailAlert` và `SMSAlert` kế thừa class cha. Thực hiện Ghi đè (Override) phương thức `gui_thong_bao` để in ra các định dạng cảnh báo khác nhau tùy theo loại hình.
