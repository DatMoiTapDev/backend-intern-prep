import re
log_rac = "Lỗi nghiêm trọng, IP tấn công là 192.168.1.99, chặn ngay!"
ket_qua = re.search(r"192\.168\.1\.99", log_rac)
print(ket_qua)
if (ket_qua):
  print(f"Phát hiện IP tấn công: {ket_qua.group()}")