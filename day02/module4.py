class Server:
    def __init__(self,name):
        self.name_of_server = name

class Router:
    def __init__(self, name):
        self.name_of_router = name
        self.list_connected = []  
    def cap_phep_ket_noi(self, server_diff):
        self.list_connected.append(server_diff)
        print(f"Router {self.name_of_router} đã cho phép {server_diff.name_of_server} kết nối")

Router1=Router("Router-Core")
Server1=Server("Web-App")

Router1.cap_phep_ket_noi(Server1)