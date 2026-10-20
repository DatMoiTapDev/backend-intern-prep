from datetime import datetime

# ==========================================
# 1. CLASS SERVER (Sử dụng Type Hinting)
# ==========================================
class Server:
    def __init__(self, ten_may: str, ram_gb: int, status: str = "online"):
        self.ten_may = ten_may
        self.ram = ram_gb
        self.status = status

    # TO-DO 1: Viết phương thức hiển thị thông tin trả về chuỗi (str)
    # Gợi ý: return f"[{self.status.upper()}] {self.ten_may} - RAM: {self.ram}GB"
    def lay_thong_tin(self) -> str:
        return f"[{self.status.upper()}] {self.ten_may} RAM: {self.ram}GB"


# ==========================================
# 2. CLASS HỆ THỐNG GIÁM SÁT (SystemMonitor)
# ==========================================
class SystemMonitor:
    def __init__(self):
        self.danh_sach_server = []

    # TO-DO 2: Viết hàm thêm Server vào hệ thống (List)
    def them_server(self, server: Server):
        self.danh_sach_server.append(server)

    # TO-DO 3: Viết hàm ghi log ra file
    # Gợi ý: Dùng with open chế độ "a", nối thời gian thực (datetime.now()) vào nội dung rồi ghi ra file "system_logs.txt"
    def ghi_log_su_co(self, noi_dung: str):
        with open("system_logs.txt", "a") as f:
            f.write(f"[{datetime.now()}] {noi_dung}\n")

    # TO-DO 4: Viết hàm quét toàn bộ hệ thống
    def quet_he_thong(self):
        print("\n--- BẮT ĐẦU QUÉT HỆ THỐNG ---")
        for sv in self.danh_sach_server:
            # 1. In ra thông tin server (gọi hàm lay_thong_tin)
            print(sv.lay_thong_tin())
            # 2. Kiểm tra nếu sập:
            # Nếu sv.status == "offline", in ra Cảnh báo và gọi hàm ghi_log_su_co()
            if sv.status == "offline":
                print(f"CẢNH BÁO: Server {sv.ten_may} đang OFFLINE")
                self.ghi_log_su_co(f"Server {sv.ten_may} đang OFFLINE")
            # 3. Kiểm tra nếu RAM thấp:
            # Dùng try-except để bắt lỗi ValueError (lỡ may lúc tạo server nhập RAM là chữ "Tám" thay vì số 8)
            # Trong phần try: Nếu int(sv.ram) < 2, in ra Cảnh báo và gọi hàm ghi_log_su_co()
            try:
                if int(sv.ram) < 2:
                    print(f"CẢNH BÁO: Server {sv.ten_may} RAM quá thấp ({sv.ram}GB)")
                    self.ghi_log_su_co(f"Server {sv.ten_may} RAM quá thấp ({sv.ram}GB)")
            except ValueError:
                print(f"LỖI: Dữ liệu RAM của Server {sv.ten_may} không hợp lệ")
                self.ghi_log_su_co(f"Server {sv.ten_may} có dữ liệu RAM không hợp lệ")

# ==========================================
# 3. THỰC THI (CHẠY CHƯƠNG TRÌNH)
# ==========================================
# 1. Khởi tạo Hệ thống
he_thong = SystemMonitor()

# 2. Khởi tạo các Server
sv_web = Server("Web-App", 8, "online")
sv_db = Server("Database-Main", 16, "offline") # Con này chết
sv_cache = Server("Redis-Cache", 1, "online")   # Con này RAM quá yếu
sv_loi = Server("Server-Loi", "Hai", "online") # Con này dữ liệu RAM bị sai (chữ "Hai")

# 3. Thêm vào hệ thống
he_thong.them_server(sv_web)
he_thong.them_server(sv_db)
he_thong.them_server(sv_cache)
he_thong.them_server(sv_loi)

# 4. Chạy quét
he_thong.quet_he_thong()