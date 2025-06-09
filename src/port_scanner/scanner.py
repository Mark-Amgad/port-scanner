import socket
from typing import List
from .models import ScanConfig


def scan_ports(config: ScanConfig) -> List[int]:
    open_ports = []
    for port in range(config.start_port, config.end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(config.timeout)
            result = s.connect_ex((str(config.host), port))
            print(f"checking port {port}")
            if result == 0:
                open_ports.append(port)
    return open_ports
