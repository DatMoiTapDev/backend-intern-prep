danh_sach_server = ["online", "offline", "online", "online", "offline", "online"]

def check_tong_server(danh_sach_server):
  tong_online = 0
  tong_offline = 0
  for sv in danh_sach_server:
    if sv == "online":
      tong_online+=1
    else:
      tong_offline+=1
  print(f"Tổng số server online: {tong_online}")
  print(f"Tổng số server offline: {tong_offline}")

check_tong_server(danh_sach_server)

