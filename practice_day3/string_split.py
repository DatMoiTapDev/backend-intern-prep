raw_ips = "192.168.1.1, 10.0.0.1, 192.168.1.2, 8.8.8.8"
def tach_chuoi(raw_ips):
    for x in raw_ips.split(", "):
        if x.startswith("192"):
            print(x)

tach_chuoi(raw_ips)