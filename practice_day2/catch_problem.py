db_config = {"host": "localhost", "port": 5432, "user": "admin"}

try:
    print(db_config["password"])
except KeyError:
    print("Lỗi: Chưa cấu hình mật khẩu cho Database!")

print("Chương trình vẫn tiếp tục chạy...")