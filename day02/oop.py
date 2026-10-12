'''
Đề bài:
1. Tạo một bản vẽ tên là Class Server.
2. Hàm khởi tạo __init__ nhận 2 đầu vào: hostname (tên máy chủ) và os (hệ điều hành).
3.Viết thêm một hành động (hàm) đặt tên là hien_thi_thong_tin(self). Hành động này sẽ in ra câu: "Server [hostname] đang chạy hệ điều hành [os]".
4.Tạo ra 2 server thật (2 object) từ Class đó:
    Server 1: hostname là "Web-App", os là "Ubuntu 22.04"
    Server 2: hostname là "Database", os là "CentOS 8"
5.Gọi hành động hien_thi_thong_tin() của cả 2 server đó để in kết quả ra màn hình.
'''

class Server:
    def __init__(self, hostname, os):
        self.ten_may_chu = hostname
        self.he_dieu_hanh = os
    def hien_thi_thong_tin(self):
        print(f"Server {self.ten_may_chu} đang chạy hệ điều hành {self.he_dieu_hanh}")

Server1 = Server("Web-App", "Ubuntu22.04")
Server2 = Server("Database", "CentOS8")

print(Server1.hien_thi_thong_tin())
print(Server2.hien_thi_thong_tin())