ips = ["192.168.1.1", "8.8.8.8", "192.168.1.2", "1.1.1.1"]
local_ips = [ip for ip in ips if ip.startswith("192.")] #biến for biến in danh_sach if điều_kiện
print(f"Bài 1 - Các IP nội bộ: {local_ips}")