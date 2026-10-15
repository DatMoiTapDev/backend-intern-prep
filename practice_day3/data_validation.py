ports_dau_vao = [80, 443, "8080a", 3306]

def check_ports(ports_dau_vao):
    for port in ports_dau_vao:
        try:
            port_chuan=int(port)
            print(f"Port hợp lệ: {port_chuan}")
        except ValueError:
            print(f"Lỗi: Port {port} chứa ký tự không hợp lệ!")

check_ports(ports_dau_vao)