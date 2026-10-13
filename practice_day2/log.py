system_logs = [
    "INFO: 192.168.1.1 - Khởi động thành công",
    "ERROR: 10.0.0.5 - Quá tải CPU",
    "INFO: 8.8.8.8 - Ping OK",
    "ERROR: 192.168.1.10 - Mất kết nối Database"
]
def xu_ly_chuoi(system_logs):
    for log in system_logs:
        if "ERROR" in log:
            print(log)
xu_ly_chuoi(system_logs)