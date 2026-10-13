class Server:
    def __init__(self, name):
        self.ten=name
        self.requests = 0
    def nhan_request(self):
        self.requests +=1
        print(f"Server {self.ten} đang xử lý request. Tổng số: {self.requests}")

class LoadBalancer:
    def __init__(self):
        self.danh_sach_server =[]
    def them_server(self, server_moi):
        self.danh_sach_server.append(server_moi)
    def phan_bo_tai(self):
        for server in self.danh_sach_server:
            server.nhan_request()

sv01=Server("Web-01")
sv02=Server("Web-02")
lb=LoadBalancer()
lb.them_server(sv01)
lb.them_server(sv02)
lb.phan_bo_tai()
lb.phan_bo_tai()