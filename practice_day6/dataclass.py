from dataclasses import dataclass
@dataclass
class ServerNode:
  ten_may:str
  ip_address: str
  ram_gb: int
  status: str = "online"

node1=ServerNode("DB-01", "10.0.0.5", 32)
print(node1.ten_may)
print(node1)