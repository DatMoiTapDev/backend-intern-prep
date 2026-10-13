servers = [
    {"name": "Server-A", "ram": 2048},
    {"name": "Server-B", "ram": 512},
    {"name": "Server-C", "ram": 1024}
]

def tim_server_yeu_nhat(danh_sach):
    server_yeu_nhat=danh_sach[0]
    for server in danh_sach:
        if server["ram"]<server_yeu_nhat["ram"]:
            server_yeu_nhat=server
    print(f"Cần cung cấp RAM cho {server_yeu_nhat['name']} vì chỉ có {server_yeu_nhat['ram']} MB")
tim_server_yeu_nhat(servers)