danh_sach_ip = ["192.168.1.1", "8.8.8.8", "10.0.0.5", "192.168.1.100", "1.1.1.1"]
for ip in danh_sach_ip:
    if ip.startswith("192.168."):
        print(f"IP nội bộ: {ip}")