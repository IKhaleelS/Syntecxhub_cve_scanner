import socket
from concurrent.futures import ThreadPoolExecutor

def scan_single_port(target, port):

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        sock.close()

        if result == 0:
            return port

    except:
        pass

    return None


def scan_ports(target, start_port, end_port, threads=100):

    open_ports = []

    with ThreadPoolExecutor(max_workers=threads) as executor:

        ports = range(start_port, end_port + 1)

        results = executor.map(lambda p: scan_single_port(target, p), ports)

        for port in results:
            if port:
                open_ports.append(port)

    return open_ports
