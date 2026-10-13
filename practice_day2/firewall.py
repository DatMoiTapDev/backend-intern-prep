firewall_ports = {"SSH": 22, "HTTP": 80, "HTTPS": 443}
firewall_ports["MySQL"]="3306"
firewall_ports["HTTP"]="8080"
del firewall_ports["SSH"]
print(firewall_ports)