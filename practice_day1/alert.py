class CanhBao:
    def __init__(self, content):
        self.noi_dung=content
    def gui_thong_bao(self):
        print(f"Đang gửi cảnh báo...")

class EmailAlert(CanhBao):
    def gui_thong_bao(self):
        print(f"Gửi Email: {self.noi_dung}")

class SMSAlert(CanhBao):
    def gui_thong_bao(self):
        print(f"Gửi tin nhắn SMS: {self.noi_dung}")

eal_01=EmailAlert("Server sập rồi")
smsa_01=SMSAlert("Server sập rồi")
eal_01.gui_thong_bao()
smsa_01.gui_thong_bao()