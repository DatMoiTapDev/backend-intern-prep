servers = [
    {"name": "Server-1", "status": "online", "ram": 512},
    {"name": "Server-2", "status": "offline", "ram": 2048},
    {"name": "Server-3", "status": "online", "ram": 4096},
    {"name": "Server-4", "status": "online", "ram": 1024}
]

def tim_server(servers):
    for server in servers:
        if server["status"] == "online" and server["ram"] >= 1024:
            print(server["name"])

tim_server(servers)