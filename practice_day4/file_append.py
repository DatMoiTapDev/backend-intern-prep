def ghi_log(noi_dung):
    with open("server_logs.txt", "a", encoding="utf-8")as file:
        file.write(noi_dung+"\n")

ghi_log("Lỗi: Server Database quá tải lúc nửa đêm!")
