# Practice Day 5: Giao tiếp với thế giới bên ngoài (API & JSON)

## 🎯 Mục tiêu
Học cách giấu thông tin nhạy cảm khỏi mã nguồn (Biến môi trường), chuyển đổi qua lại giữa Python Dictionary và JSON, và đặc biệt là kỹ năng cốt lõi của Backend: Gọi API qua giao thức HTTP.

## 📝 Đề bài
**Bài 1: Bảo mật với Biến môi trường (`os`)**
Sử dụng thư viện `os` để đọc các thông số nhạy cảm (như API_KEY) thay vì gõ thẳng (hardcode) vào file Python.

**Bài 2: Từ điển sang JSON (Serialization)**
Sử dụng thư viện `json` để biến một Dictionary của Python thành chuỗi JSON chuẩn mực (có thụt lề cho đẹp).

**Bài 3: JSON sang Từ điển (Deserialization)**
Nhận một chuỗi JSON mô phỏng từ một hệ thống khác gửi tới, dùng `json` để biến nó thành Dictionary và bóc tách dữ liệu.

**Bài 4: Lần đầu gọi API (`requests`)**
Cài đặt thư viện `requests`. Thực hiện một lệnh HTTP GET lên một API công khai (JSONPlaceholder) để lấy thông tin của một User thật trên mạng.

**Bài 5: OOP - Xây dựng API Client**
Tạo `class GithubUserAPI`. Hàm khởi tạo nhận vào username GitHub của em. Viết hàm kết nối lên API của GitHub để lấy ra số lượng Follower và Public Repo của em.