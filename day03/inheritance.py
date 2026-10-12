class NhanVien:
    def __init__(self, ten, luong_co_ban):
        self.ten=ten
        self.luong=luong_co_ban
    def hien_thi_thong_tin(self):
        print(f"Nhân viên {self.ten}, Lương: {self.luong} VNĐ")

class KySuCloud(NhanVien):
    def trien_khai_server(self):
        print(f"Kỹ sư {self.ten} đang cấu hình máy chủ trên AWS!")

ks_01=KySuCloud("Tiến Đạt", "20.000.000")
ks_01.hien_thi_thong_tin()  
ks_01.trien_khai_server()  