server_hien_tai = {"name": "DB-Main", "status": "offline", "cpu": "99%"}
def khoi_dong_lai(thiet_bi):
    thiet_bi["status"] = "online"
    thiet_bi["cpu"] = "10%"
    print(f"{thiet_bi['name']} đã được Reboot. Trạng thái: {thiet_bi['status']}, CPU: {thiet_bi['cpu']}")
khoi_dong_lai(server_hien_tai)
