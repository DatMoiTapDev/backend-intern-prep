from dataclasses import dataclass
@dataclass
class NhanVien:
  id:int
  ten:str
  chuc_vu:str
def lay_thong_tin_nhan_vien(nv_id:int) -> NhanVien:
  if nv_id==1:
    return NhanVien(1, "Tiến Đạt", "Backend Intern")
  return NhanVien(nv_id, "Unknow", "Guest")

dat=lay_thong_tin_nhan_vien(1)
print(dat.ten, dat.chuc_vu)