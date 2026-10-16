class DatabaseConfig:
  def __init__(self, host, port, user):
    self.host = host
    self.cong = port
    self.nguoidung = user
  def tao_file_cau_hinh(self):
    with open("db_config.txt","w") as file:
      file.write(f"Host: {self.host}\n")
      file.write(f"Port: {self.cong}\n")
      file.write(f"User: {self.nguoidung}\n")
db_dev=DatabaseConfig("localhost", 3306, "root")
db_dev.tao_file_cau_hinh()