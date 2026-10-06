# Danh sách dữ liệu đầu vào
switches = [
    {"name": "Switch-Floor1", "port_speed": 1000},
    {"name": "Switch-Floor2", "port_speed": 100},
    {"name": "Switch-Core", "port_speed": 10000} 
]
'''
Đề bài
Anh có một danh sách các thiết bị Switch cần quản lý, em hãy:
1.Viết một Hàm (Function): Tên hàm là kiem_tra_thiet_bi. 
2.Hàm này nhận đầu vào là một list chứa danh sách các thiết bị (như biến switches bên dưới).
Nếu thiết bị nào có port_speed (Tốc độ cổng) là 1000 (Gigabit), 
thì in ra câu: "Thiết bị [Tên] đạt chuẩn Gigabit". 
Nếu là 100 thì in ra "Thiết bị [Tên] quá cũ".
'''

def kiem_tra_thiet_bi(switch_list):
    for switch in switch_list:
        if switch["port_speed"] >= 1000:
            print(f"Thiết bị {switch['name']} đạt chuẩn Gigabit")
        else: print(f"Thiết bị {switch['name']} quá cũ")

kiem_tra_thiet_bi(switches)