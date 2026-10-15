class Server:
  def __init__(self, name, status):
    self.ten = name
    self.status = status
class SystemMonitor:
  def __init__(self):
    self.danh_sach_quan_ly=[]
  def them_server(self, server):
    self.danh_sach_quan_ly.append(server)
  def quet_he_thong(self):
    for sv in self.danh_sach_quan_ly:
      if sv.status == "offline":
        print(f"Cảnh báo: Server {sv.ten}đang sập!")

sv01=Server("Windows", "offline")
sv02=Server("Linux", "online")
sv03=Server("Ubuntu", "offline")
sm01=SystemMonitor()
sm01.them_server(sv01)
sm01.them_server(sv02)
sm01.them_server(sv03)
sm01.quet_he_thong()

