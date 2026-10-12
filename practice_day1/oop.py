class TaiKhoan:
    def __init__(self, username, role):
        self.ten=username
        self.vai_tro=role
    def kiem_tra_quyen(self):
        if self.vai_tro=="admin":
            print(f"Được xóa Database")
        else:
            print(f"Chỉ được xem dữ liệu")
tk_01=TaiKhoan("dat","admin")
tk_02=TaiKhoan("tu","user")
tk_01.kiem_tra_quyen()
tk_02.kiem_tra_quyen()
